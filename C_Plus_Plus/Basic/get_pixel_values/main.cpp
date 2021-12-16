#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {
    std::cout << "Hello, world!\n";
    cv:: Mat Image ;
    Image = cv::imread("C:/Users/Asadullah/Projects/Opencv/Course/coding_pubic/learn-opencv-python/images/shapes_image.png");
    
    cv::imshow("image", Image);
    cv::waitKey(0);
    return 0;

}
