#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {
    cv::Mat img, resize;
    // int width = 300; 
    // int height = 300;
    std::string path_img = "C:/Users/Asadullah/Pictures/Lenna.png";
    img = cv::imread(path_img);
    cv::imshow("img", img);
    cv::waitKey();

}
