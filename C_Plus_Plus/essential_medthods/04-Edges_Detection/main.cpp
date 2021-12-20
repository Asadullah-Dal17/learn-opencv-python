#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {

    // declearing the variables
    cv::Mat img, edges, gray, blur_img;
    
    img = cv::imread("C:/Users/Asadullah/Pictures/Lenna.png");
    cv::cvtColor(img, gray, cv::COLOR_BGR2GRAY);
    cv::GaussianBlur(gray, blur_img, cv::Size(5,5),0);
    cv::Canny(blur_img, edges, 40, 200, 3, false);
    cv::imshow("Canny", edges);

    cv::imshow("img", img);
    cv::waitKey();   

}
