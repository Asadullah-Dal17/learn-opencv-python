#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    // std::cout << "Hello, world!\n";
    // reading image from dir 
    std::string path_img = "C:/Users//Asadullah/Pictures/Lenna.png";
    cv:: Mat img ;
    cv:: Mat blured, blured2;
    img =cv::imread(path_img);
    // bluring the image 
    cv::blur(img, blured, cv::Size(13,13));
    cv::blur(img, blured2, cv::Size(33,33));

    cv::imshow("blured image", blured);
    cv::imshow("blured2 image", blured2);


    cv::imshow("img", img);
    cv::waitKey();
}
