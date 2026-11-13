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