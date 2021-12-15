#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    std::string image_path ="C:/Users/Asadullah/Projects/Opencv/Course/coding_pubic/learn-opencv-python/images/shapes_image.png";
    
    std::string saving_path ="C:/Users/Asadullah/Projects/Opencv/Course/coding_pubic/learn-opencv-python/C_Plus_Plus/Basic/save_image/save_image.png";

    // std::cout<<test;
    cv::Mat image; // creating Mat data type for image
    image = cv::imread(image_path,0);
    cv::imwrite(saving_path, image);
    cv::imshow("Images", image); //showing image on screen
    cv::waitKey(0); // making window wait until key is pressed on keyboard
    cv::Mat loading_saved = cv::imread(saving_path);
    cv::imshow("saved_image",loading_saved);
    cv::waitKey(0);
    return 0;
}
