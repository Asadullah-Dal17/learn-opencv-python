#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    // cv::Mat img ;
    std::cout<<"done";
    int width =640;
    int height =480;
    // cv::Scalar color  = (0,255,0);
    cv::Mat img(height, width, CV_8UC3, cv::Scalar(0,0,0));

    cv::imshow("img", img);
    cv::waitKey();
}
