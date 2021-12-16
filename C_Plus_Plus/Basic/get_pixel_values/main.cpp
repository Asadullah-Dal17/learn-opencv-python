#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {
    std::cout << "Hello, world!\n";
    cv:: Mat Image;
    Image = cv::imread("C:/Users/Asadullah/Projects/Opencv/Course/coding_pubic/learn-opencv-python/images/shapes_image.png");
    // getting the pixel values 
    int b = Image.at<cv::Vec3b>(10, 10)[0];
    int g = Image.at<cv::Vec3b>(10, 10)[1];
    int r = Image.at<cv::Vec3b>(10, 10)[2];

    std::cout<<"BLUE values  "<<b<<std::endl;
    std::cout<<"GREEN values  "<<g<<std::endl;
    std::cout<<"RED values  "<<r<<std::endl;
    std::cout<<"-------- \n --------- \n -------- \n --- ";


    cv::imshow("image", Image);
    cv::waitKey(0);
    return 0;

}
