#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {

    // declearing the variables
    cv::Mat img, edges, gray;
    img = cv::imread("C:/Users/Asadullah/Pictures/Lenna.png");
    cv::imshow("img", img);
    cv::waitKey();   

}
