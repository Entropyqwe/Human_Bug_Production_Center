以下为API

1.nameWindow()标注好名字，用于创建窗口
*视频就是若干的图片在一个窗口中进行显示（播放）
namewindow（名字，类型）
WindowFlags {
1.1WINDOW_NORMAL
) / also use to switch a fullscreen window to a normal size.
1.2WINDOW_AUTOSIZE
s constrainted by the image displayed.

2.imshow()
参数一：窗口的名字
void imshow(const String& winname, InputArray mat);

3.destroyAllWindows()
删除掉原本创建的窗口

4.resizeWindow
用来调节窗口的大小，默认为图片的大小
void resizeWindow(const String& winname, int width, int height);
第一项是窗口的名字，第二项是窗口的宽度，第三项是窗口的高度

5.using namespace cv（c++写法）;
from cv2 import * （python写法，必须带上星号）；可以避免反复写cv2.

6.cv2.waitKey(0)在运行过程中实际上会返回一个值，这个值可以进行变量定义
key=cv2.waitKey(0)
if(key=='q'):
    exit()
7.加载图片
imread
im==image
imread(path,flag)
flag的形式有如下
IMREAD_GRAYSCALE图片输出为灰色
IMREAD_COLOR图片输出为彩色
不进行定义的话默认是彩色的


视频采集
VideoCapure()
（设备名字，API选择）
第一个摄像头标号都是0，其他以此进行标注，括号内写标号

cap.read读出采集的视频资源
会返回两个值
第一个值是状态值，当读到到视频帧为true；第二个值是是视频帧

cap.release()释放出我们过程中所占据的资源

视频录制
添加头文件 fourcc=cv2.VideoWriter_fourcc('*MJPG')
VideoWriter
参数：第一个是输出文件名字，第二个是多媒体文件格式（编码器），多为VideoWriter_fourcc,第三个为帧率，第四个为分辨率率大小
write写入文件（将原始的数据压缩编码后再写入）
要求：写入视频帧数，分辨率
release
