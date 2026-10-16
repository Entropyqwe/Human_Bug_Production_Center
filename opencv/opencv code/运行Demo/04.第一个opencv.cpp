#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;

int main()
{
    Mat image = imread("data/example.png");
    if (image.empty()) {
        std::cerr << "Failed to load data/example.png" << std::endl;
        return 1;
    }

    namedWindow("example", WINDOW_AUTOSIZE);
    imshow("example", image);
    waitKey(0);
    return 0;
}