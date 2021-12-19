#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {

    cv::Mat img, region, blurred_region;
    // region points
     int x, y , width, height ; 
    x =140; y =216; width = 240; height =200;

    img = cv::imread("C:/Users/Asadullah/Pictures/Lenna.png");
    cv::Rect crop_region(x, y, width, height );
    region = img(crop_region);
    cv::blur(region, blurred_region, cv::Size(13,13));
    cv::imshow("blured_region",blurred_region);
    cv::imshow("Region", region);
    cv::imshow("img", img);
    cv::waitKey();

}
