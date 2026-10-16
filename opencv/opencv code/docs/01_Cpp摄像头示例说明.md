程序打开第一个摄像头，循环读取画面并显示；按 `Esc` 或 `q` 退出，最后释放资源。
#include <opencv2/opencv.hpp>
引入 OpenCV 总头文件，使程序认识 `VideoCapture`、`Mat`、`imshow` 等功能。
#include <iostream>

引入 C++ 输入输出库，使程序可以使用 `cout` 和 `endl`。


using namespace cv;
using namespace std;

允许直接写 `Mat`、`VideoCapture`、`cout`。否则要写成 `cv::Mat`、`std::cout`。

int main()
{
`main` 是程序入口，大括号中的代码会按顺序执行。

VideoCapture cap(0);
创建摄像头对象。参数 `0` 通常代表第一个摄像头，第二个通常是 `1`。
```cpp
if (!cap.isOpened()) {
```
检查摄像头是否打开成功。`isOpened()` 成功时为真，`!` 表示取反。
```cpp
cout << "Error: Could not open camera" << endl;
```
在终端输出错误信息；`endl` 表示换行并刷新输出。
```cpp
return -1;
```
摄像头打不开时结束程序。非零返回值通常表示出错。
```cpp
Mat img;
``
创建图像变量。`Mat` 是 OpenCV 表示图像和矩阵的核心类型。
```cpp
namedWindow("img", WINDOW_NORMAL);
```
创建名为 `img` 的窗口，`WINDOW_NORMAL` 允许调整大小。
```cpp
while (1)
``
开始无限循环。`1` 表示真，遇到 `break` 才会结束。
```cpp
cap >> img;
```
从摄像头读取一帧并保存到 `img`，也可以写成 `cap.read(img)`。
```cpp
if (img.empty())
    break;
```
检查图像是否为空。读取失败时跳出循环。
```cpp
imshow("img", img);
```
把图像显示在名为 `img` 的窗口中。
```cpp
char key = waitKey(20);
```
等待 20 毫秒，同时刷新窗口并接收键盘输入。
```cpp
if (key == 27 || key == 'q')
```
判断是否按下 `Esc`（常见编码为 27）或字母 `q`。`||` 表示“或者”。
```cpp
break;
```
跳出循环。
```cpp
cap.release();
destroyAllWindows();
``
释放摄像头并关闭所有 OpenCV 窗口。
```cpp
return 0;
```
返回 `0` 表示程序正常结束。
## 调用摄像头的方法论

按照下面顺序组织程序：

1. **打开设备**：`VideoCapture camera(0)`。
2. **检查状态**：调用 `isOpened()`，失败就输出错误并退出。
3. **读取画面**：循环调用 `read(frame)` 或 `cap >> frame`。
4. **检查图像**：判断 `read` 是否成功，以及 `frame.empty()` 是否为假。
5. **处理图像**：可使用 `resize`、`cvtColor`、`GaussianBlur`、`Canny` 等函数。
6. **显示图像**：使用 `imshow`。
7. **监听退出**：使用 `waitKey` 检测 `Esc` 或 `q`。
8. **释放资源**：调用 `release` 和 `destroyAllWindows`。

推荐模板：

```cpp
cv::VideoCapture camera(0);
if (!camera.isOpened()) return -1;

cv::Mat frame;
while (true) {
    if (!camera.read(frame) || frame.empty()) break;
    cv::imshow("Camera", frame);
    int key = cv::waitKey(20);
    if (key == 27 || key == 'q' || key == 'Q') break;
}

camera.release();
cv::destroyAllWindows();
```

## 常见问题

### 找不到头文件

错误 `opencv2/opencv.hpp: No such file or directory` 表示没有添加头文件目录：

```text
-ID:/opencv/build/x64/mingw5/install/include
```

### 找不到库

添加库目录并链接 OpenCV 库：

```text
-LD:/opencv/build/x64/mingw5/install/x64/mingw/lib
-lopencv_highgui500 -lopencv_videoio500 -lopencv_imgproc500 -lopencv_core500
```

### 缺少 DLL

把下面目录加入 `PATH`：

```text
D:/opencv/build/x64/mingw5/install/x64/mingw/bin
C:/msys64/ucrt64/bin
```

### 无法打开摄像头

关闭微信、QQ、浏览器等占用摄像头的软件；检查 Windows 摄像头权限；再尝试把编号 `0` 改成 `1`。

### 窗口不刷新

`imshow` 后必须调用 `waitKey`，否则窗口可能不刷新或无法响应按键。

## 记忆口诀

```text
打开设备 → 检查状态 → 读取一帧 → 检查图像
→ 处理图像 → 显示图像 → 等待按键 → 释放资源
```