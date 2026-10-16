#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;

int main()
{
    Mat image=imread(R"(C:\Users\23832\OneDrive\图片\Xbox Screenshots\《光环：无限》-2022_07_01-07_36_22.png);
    if(image.empty()){
    std::cout<<"失败"<<std::end1;
    return -1;
    }
    nameWindow("example",WINDOW_AUTOSIZE);
    imshow("example",image);
    waitKey(0);
    return 0;
}
