按照识别流程划分

1.cvtColor函数用于进行色彩转换
标准格式    cvtColor(原图变量，转换类型，输出标准)
例子：转出灰图——cvtColor(str gray,COLOR_BGR3GRAY);
换成HSV模式输出———cvtColor(str hsv,COLOR_BGRHSV);

2.范围筛选函数
将符合图像所给范围内的相续统一进行转换
假如：将目标全部转化为白色，即为1，不需要的部分全部转换为0即为黑色
此操作称为掩膜（mask），覆盖掉不需要的一部分
描述范围（inrange和scalar函数）
cv::inRange(hsv,cv::Scalar(35,80,50)//H S V三个通道的下限分别为所填数字
            cv::Scalar(85,255,255),mask)
            上线分别是85，255，255
            其余的地区掩盖成黑色

3.全局阈值函数
double cvs:threshold (InputArray src, 
OutputArray dst, 
double thresh, 
double maxval, 
int type
大于阈值的输出阈值，小于阈值的输出本身
或者超出阈值的进行输出，没有超过的则不输出
现实比喻：rm中的灯条亮度极高，通过标定灯条边界来获得目标板位置
实际输入：
cv.threshold(gray,mask,120,255,cv::THRESH_BINARY);
第五个参数决定了针对什么阈值进行输出，是过亮的还是过暗的？
还会有很多问题，阴影怎么办

4.局部阈值函数，通过自适应合适的阈值进行判断，来进行不同区域有区分度的掩膜工作

5.自动全局阈值
参考摄影的灰度直方图
通过阅读直方图来了解哪一个值可以最大限度地分开前景和后景，分开两个峰
大津法