#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {
    cv::Mat img, resized_img;
    int width = 300; 
    int height = 300;
    std::string path_img = "C:/Users/Asadullah/Pictures/Lenna.png";
    // reszing the image 
    img = cv::imread(path_img);
    cv::resize(img, resized_img, cv::Size( width, height), cv::INTER_LINEAR);
    cv::imshow("Resized Img", resized_img);

    img = cv::imread(path_img);
    cv::imshow("img", img);
    cv::waitKey();

}
