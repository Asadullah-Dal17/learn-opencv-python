#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    // creating the image path 
    std::string img_path ="C:/Users/Asadullah/Pictures/color_Square.png";
    // creating the empty image 
    cv::Mat img;
    img = cv::imread(img_path);
    // creating Mat for gray scale image 
    cv::Mat gray;
    // converting the color image to gray scale image 
    cv::cvtColor(img, gray, cv::COLOR_BGR2GRAY);
    // displaying the image using imshow function from opencv python 
    cv::imshow("gray", gray);
    cv::imshow("img", img);
    cv::waitKey();
    
    }
