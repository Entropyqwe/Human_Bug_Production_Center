## 1.文件转移没有完全转移
之所以没有转移，是因为 CMake 有个小脾气：它会“记住”你第一次编译时的设置。
为什么会出现这种情况？

    你可能在更早之前，在 project2 目录下执行过一次 cmake .（注意是一个点 .）。
    那次操作在 project2 里留下了一个“记录文件”（缓存）。
    当你后来创建了 build 文件夹，并试图在 build 里执行 cmake .. 时，CMake 发现了那个旧的“记录文件”，它以为你想沿用旧的设置，于是自作聪明地把新文件又扔回了 project2 目录。

怎么解决？
我们必须手动删掉那个旧的“记录文件”，强制让 CMake 重新认识我们在 build 里操作。
请在终端里依次输入以下三行命令：
cd .. 
rm -rf CMakeCache.txt CMakeFiles/ 
cd build

cmake ..
### 2.命令必须在相应的目录下进行生成
### 3.关于进程与文件的执行
文件执行必须是当前文件夹下面的可执行文件
find . -type f -executable
查看真正的可执行文件
正确的运行前顺序
./build/main
或者使用
cd build ./main
### 4.cd只能打开文件夹，而cat用来打开特定的文件
### 5.必须要先创建一个CML文件，终端是看不懂CML文件里面填写的东西的
touch CMakeLists.txt






