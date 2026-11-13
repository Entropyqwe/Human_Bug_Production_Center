允许开发者指定整个工作的编译流程，在根据编译平台自动生成本地化的makefile和工程文件

为什么需要？
项目一旦变大，比如k210 Stm32这一类的项目文件过多，包括烧录文件，批量进行编译会方便许多
Makefile 的好处是：

- **自动判断哪些文件被改过**，只重新编译改动的部分；
- **管理依赖关系**，比如某个 `.c` 依赖某个 `.h`；
- **一键编译**，不用每次敲很长命令；
- **支持多个目标**，比如 `make build`、`make clean`、`make flash`

例子：app: main.c utils.c
		gcc main.c utils.c -o app
		意思是如果第一行的两个文件被修改过，就在下面重新生成编译文件，一般使用gcc进行编译为可执行文件app
	指定文件是第一行做的事情，而第二行是命令行，命令行之前必须使用Tab空位

通常的构建的顺序是将源代码和执行文件转化为可以直接运行的执行文件
顺序：源文件-预处理-编译-汇编-链接-打包部署

在很多项目中，包含烧录文件一类，包含有成百上千的文件，不好进行手动编译，所以使用这一类编译工具进行批量编译
将CMAKE当作是一个自动生成makefile的工具
优点
跨平台
能够管理大型项目
简化编译构建过程和编译过程
可扩展：可以为 cmake 编写特定功能的模块，扩充 cmake 功能### 但是makefile不能够跨平台

所以引入Cmake进行处理

#### 对于cmake的构建缓存，在新加入文件后一定要进行释放并且重新构建
删除旧的构建缓存
rm -rf CMakeFiles CMakeCache.txt Makefile（在cmake中的操作属于是强制删除的操作）
重新生成构建系统
cmake .
重新编译
make

直接针对文件进行写入
echo '#include <iostream> 
int main() { 
std::cout << "Hello, World!" << std::endl;
return 0; 
}' > main.cpp

echo回声，>main.cpp传入这个文件
直接使用这个格式进行写入，一般来讲，前面会先进行删除操作

rm -f main.cpp

清理Cmake缓存
rm -rf CMakeCache.txt CMakeFiles Makefile && cmake .
重新编译
make
运行程序
运行程序是./app
小提醒：
	在c++中
	std::cout << "Hello, World!" << std::endl；
	等同于在C当中的printf输出
	区别：在C++中的这种写法不需要考虑输出的类型（不需要考虑是整数还是浮点数）
	cout是标准类型输出，它会自动匹配相关的类型并且给予输出的操作

###  执行顺序
先创建Cmake文件
vim CMakeLists.txt
将需要编辑的文件放在一起
添加CmakeList文件，作为初始的文件设置
cmake_minimum_required(VERSION 3.0)
project(CALC)
add_executable(app add.c div.c main.c mult.c sub.c)
执行cmake命令

如果想要批量地进行编辑
创建一个文件夹
mkdir 文件名
进入文件夹
在新的文件夹中执行cmake..将中间文件和可编辑文件进行整理
再执行make编辑命令，最后可以使用./app进行执行


在编译过程中会产生一些和项目无关的编译文件，这些是中间文件和可执行文件，要将这些文件进行重新分类
1,先创建一个新的文件夹
mkdir
为make directory的缩写
创建完成后进入到文件夹中
使用cmake ..返回到上一级的文件夹，将中间文件重新进行收录
tree build-L1是指查看build文件夹下面的第一级目录

## 在Cmake中一定要注意有关的空格：
例子：
cmake ..在这里中间必须有空格，这是指在上一个目录中执行Cmake命令，不是连载一起的，中间必须要有空格
tree build -L1:在build和L1之间也必须要有空格，因为二者不是一个整体，可以理解为是附加词

### 定义变量
在cmake中进行定义使用set
# 方式1: 各个源文件之间使用空格间隔
# set(SRC_LIST add.c  div.c   main.c  mult.c  sub.c)

# 方式2: 各个源文件之间使用分号 ; 间隔
set(SRC_LIST add.c;div.c;main.c;mult.c;sub.c)
add_executable(app  ${SRC_LIST})
在set语法中第一个就是设置的变量名

一般使用C++作为编写标准
$ g++ *.cpp -std=c++11 -o app,将C++11作为执行标准，这是在进行C++编写时做的

在Cmake中
直接在CmakeList中进行制订
#增加-std=c++11
set(CMAKE_CXX_STANDARD 11)
#增加-std=c++14
set(CMAKE_CXX_STANDARD 14)
#增加-std=c++17
set(CMAKE_CXX_STANDARD 17)

### 搜索文件
使用aux_source_directory命令或者file命令。
例子
aux_source_directory(< dir > < variable >)
dir是要查找的目录，variable是一个变量，负责将从dir目录下搜索到的文件存储到这一个变量当中
在cmakeList文件下面进行操作
cmake_minimum_required(VERSION 3.0)
project(CALC)
include_directories(${PROJECT_SOURCE_DIR}/include)
# 搜索 src 目录下的源文件
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src SRC_LIST)
add_executable(app  ${SRC_LIST})

${CMAKE_CURRENT_SOURCE_DIR}当前处理的Cmake文件所在的初始目录
方法二

file(GLOB/GLOB_RECURSE 变量名 要搜索的文件路径和文件类型)
GLOB: 将指定目录下搜索到的满足条件的所有文件名生成一个列表，并将其存储到变量中。
GLOB_RECURSE：递归搜索指定目录，将搜索到的满足条件的文件名生成一个列表，并将其存储到变量中。
file(GLOB MAIN_SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)
file(GLOB MAIN_HEAD ${CMAKE_CURRENT_SOURCE_DIR}/include/*.h)



在命令行中创建可读文件
ls -la | tee 主题1.log
### 在命令行中直接打开某个文件
nano语句

### 在动态库之前


┌──────────── 构建期（只在 cmake / make 时发生）────────────┐
CMakeLists.txt ──读──> CMake ──生成──> build/Makefile
                                          │
include/head.h ──声明──┐                  │ make
src/add.cpp  ──编译──> add.o  ──┐         │
src/sub.cpp  ──编译──> sub.o  ──┤         │
src/mult.cpp ──编译──> mult.o ──┼──链接──> bin/app
src/div.cpp  ──编译──> div.o  ──┤
src/main.cpp ──编译──> main.o ──┘
└───────────────────────────────────────────────────────────┘
┌──────────── 运行期（./bin/app 时发生）────────────┐
bin/app ──> 内核加载 ──> main() ──> 依次调用 4 个函数
└───────────────────────────────────────────────────┘

终端输入 ./bin/app
  │
  ├─ 内核 execve 加载 ELF，动态链接器把 libc 等装进来
  ├─ 启动代码 _start → __libc_start_main
  ├─ 调用 main()
  │    ├─ a=20, b=12
  │    ├─ printf("a = ...")            ← 输出第 1 行
  │    ├─ 调用 add(20,12)   → 32
  │    ├─ printf("a + b = ...")        ← 输出第 2 行
  │    ├─ 调用 subtract(20,12) → 8
  │    ├─ printf("a - b = ...")        ← 输出第 3 行
  │    ├─ 调用 multiply(20,12) → 240
  │    ├─ printf("a * b = ...")        ← 输出第 4 行
  │    ├─ 调用 divide(20,12)  → 1.666667
  │    └─ printf("a / b = ...")        ← 输出第 5 行
  ├─ return 0 → exit() 刷新缓冲区 → 回收进程

构建期：CMake 把"5 个 .cpp + 1 个头文件目录"翻译成 Makefile，make 再把每个 .cpp 单独编译成 .o，最后链接成一个 app。运行期：操作系统只认 bin/app 这一个文件，从 main 开始按语句顺序执行，printf 去 libc 里找，add/subtract/multiply/divide 就在本进程里直接跳过去执行。头文件和 CMakeLists 都是"幕后人员"，程序跑起来时已经退场。

如果不分头文件，所有代码都堆在一个文件里，文件多了就会很乱。

分开之后：

- `.h` 头文件：**对外说“我能提供什么”**；
- `.cpp` 源文件：**内部写“我具体怎么做”**。126

比如：

- `calc.h`：声明 `add`、`sub`；
- `add.cpp`：实现 `add`；
- `sub.cpp`：实现 `sub`；
- `main.cpp`：调用 `add`、`sub`。

`include_directories(include)`，括号内是头文件所处的位置，在目标运行时，会直接从这个目录下面调取到关于一些自定义函数的声明

### 关于静态库和动态库的区别
都是只将源代码进行打包，比如在C++中，文件就是cpp
好，我用大白话逐个解释：

### 链接时机

- **静态库**：编译的时候就把库里的代码"抄"进你的程序里，抄完就完事了。
- **动态库**：编译的时候只记个笔记"我需要用这个库"，真正用的时候（程序跑起来）才去找它。

### 运行时依赖

- **静态库**：程序编译好后，那个 `.a` 文件删了也没事，程序照样跑。
- **动态库**：程序跑的时候必须能找到 `.so` 文件，找不到就报错崩溃。

### 程序体积

- **静态库**：代码被塞进程序里了，程序自然变胖。
- **动态库**：程序里只留了个"引用"，本身很瘦。

### 内存占用

- **静态库**：你开 10 个同样的程序，内存里就有 10 份库代码，各占各的。
- **动态库**：10 个程序共用同一份库代码，内存里只存一份，省空间。

### 更新方式

- **静态库**：库改了，所有用到它的程序都得重新编译，不然用的还是老代码。
- **动态库**：直接把 `.so` 文件替换掉，所有程序下次运行自动用新代码，不用重新编译。

### 部署难度

- **静态库**：发给别人一个可执行文件就够了，对方直接双击就能跑。
- **动态库**：发给别人时得确认对方电脑里有没有对应的 `.so`，没有还得一起发过去，麻烦一点。

### 一句话总结

**静态库像"把菜谱背下来自己做"，动态库像"打电话叫外卖"。** 前者独立但占地方，后者灵活但依赖外部。

### 工程中的运用

结合仿生足式机器人这类比赛，静态库和动态库其实很容易落到实际工程里。

### 例子一：把底层硬件驱动打成静态库

在仿生足式机器人比赛中，电机驱动、IMU 读取、编码器采集、CAN/UART 通信这些模块通常比较稳定，不太会频繁改动。

比如你可以把：

```text
motor_driver.cpp
imu_reader.cpp
encoder_reader.cpp
can_bus.cpp
```

打包成一个静态库：

```cmake
add_library(robot_bsp STATIC src/motor_driver.cpp src/imu_reader.cpp src/encoder_reader.cpp src/can_bus.cpp)
```

主程序再链接它：

```cmake
add_executable(foot_robot src/main.cpp src/gait_planner.cpp)
target_link_libraries(foot_robot PRIVATE robot_bsp)
```

这样做的好处是：

- 机器人上电后直接跑，不需要额外带 `.so`；
- 底层驱动一旦编译进去，不容易被误替换；
- 适合嵌入式主控、实时性要求高的场景；
- 比赛现场部署时更稳定，少出现“找不到库”的问题。

缺点就是：如果驱动库修了一个 Bug，所有用到它的程序都要重新编译。

### 例子二：把步态/视觉/地形分析模块打成动态库

仿生足式机器人通常有步态规划、逆运动学、状态估计、视觉识别、地形分析等模块。

这些模块可能会经常调参、换算法、升级模型，所以更适合做成动态库。

比如：

```cmake
add_library(gait_planner SHARED src/gait_planner.cpp src/ik_solver.cpp)
add_library(vision_detect SHARED src/foot_detect.cpp src/terrain_analyze.cpp)
```

主程序链接它们：

```cmake
add_executable(foot_robot src/main.cpp)
target_link_libraries(foot_robot PRIVATE gait_planner vision_detect)
```

这样做的好处是：

- 比赛前想换一套步态策略，只替换 `libgait_planner.so` 就行；
- 视觉识别升级后，不用重新编译整个主控程序；
- 不同队伍成员可以分别开发步态模块、视觉模块，最后通过库接口对接；
- 适合上位机、仿真环境、ROS 节点这类需要灵活升级的场景。

### 放到你的项目里可以这样理解

如果你做的是四足机器人、足式机器人、或者带视觉/地形分析的比赛项目，可以这样拆：

|模块|建议库类型|原因|
|---|---|---|
|电机、IMU、编码器、CAN 驱动|静态库|稳定、实时、部署简单|
|步态规划、逆运动学|动态库|经常调参、换算法|
|视觉识别、地形分析|动态库|模型和算法迭代快|
|主程序|可执行文件|链接上述库运行|

一句话记：  
**底层驱动求稳，用静态库；算法模块求活，用动态库。*
需要进行实时演算的实时程序需要使用动态库，而底层的相关的固件使用静态库