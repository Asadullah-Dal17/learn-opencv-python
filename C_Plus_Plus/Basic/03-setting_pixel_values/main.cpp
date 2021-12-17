#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {

std::string img_path = "C:/Users/Asadullah/Pictures/color_Square.png";
cv::Mat original_img;

original_img = cv::imread(img_path, cv::IMREAD_COLOR);

cv::Mat modifed_img = cv::imread(img_path, cv::IMREAD_COLOR);
for (int r=0; r<modifed_img.rows; r++){
    // std::cout<<" "<<r;
    for(int c =0; c<modifed_img.cols; c++){
        
    modifed_img.at<cv::Vec3b>(r, c)[0] = modifed_img.at<cv::Vec3b>(r ,c)[0] =0;

    }
}
cv::imshow("original_img", original_img);
cv::imshow("modified_img", modifed_img);
cv::waitKey();


}
