#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    // creating mat 
   cv::Mat img, img_region;
   std::string path_img = "C:/Users//Asadullah/Pictures/Lenna.png";
//    reading image from dir 
    img = cv::imread(path_img);
    int x, y , width, height ;
    // defing the values for croping region or ROI 
    x =140; y =216; width = 240; height =200;
    // selecting the region or ROI
    cv::Rect crop_region(x, y, width, height);
    // cropping the Region 
    img_region =img(crop_region);
    // display the output images  
    cv::imshow("region", img_region);
    cv::imshow("img", img);
    cv::waitKey();

}
