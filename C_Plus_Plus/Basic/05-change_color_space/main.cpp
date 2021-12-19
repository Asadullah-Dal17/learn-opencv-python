#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    // std::cout << "Hello, world!\n";
    std::string img_path ="C:/Users/Asadullah/Pictures/color_Square.png";
    cv::Mat img;
    img = cv::imread(img_path);
    // creating Mat for gray scale image 
    cv::Mat gray ;
    cv::cvtColor(img, gray, cv::COLOR_BGR2GRAY);
    cv::imshow("gray", gray);
    cv::imshow("img", img);
    cv::waitKey();
    
    }
