#include <iostream>
#include <opencv2/opencv.hpp>
int main(int, char**) {
    cv::VideoCapture cap (3);
    
if (cap.isOpened() ==false){
    std::cout<<"can't open the video"<<std::endl;
    return -1;
}
while (true){
    cv::Mat frame ;
    bool ret = cap.read(frame);
   if ( ret ==false){
       std::cout<<"Found the end of Video"<<std::endl;
       break;
   }

   cv::imshow("frame", frame);
   if (cv::waitKey(1)==27){
       std::cout<<" close the Video Stream";
       break;
   }

}

}
