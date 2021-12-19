#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    // std::cout << "Hello, world!\n";
    // reading image from dir 
    std::string path_img = "C:/Users//Asadullah/Pictures/Lenna.png";
    cv:: Mat img ;
    cv:: Mat blured_img;
    img =cv::imread(path_img);
    // bluring the image 
    cv::GaussianBlur(img, blured_img, cv::Size(33,33), 0);
    cv::imshow("blured image", blured_img);

    cv::imshow("img", img);
    cv::waitKey();
}
