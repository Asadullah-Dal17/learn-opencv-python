#include <iostream>
#include "opencv2/opencv.hpp"
using namespace std;

int main(int argc, char** argv )
{

    cv::Mat image;  // variable image of datatype Matrix
    image = cv::imread("C:/Users/Asadullah/Projects/Opencv/Course/coding_pubic/learn-opencv-python/images/shapes_image.png");

    cv::imshow("Display Image", image);
    cv::waitKey(0);
    return 0;
}