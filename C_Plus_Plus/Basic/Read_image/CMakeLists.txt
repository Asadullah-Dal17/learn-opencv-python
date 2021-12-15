cmake_minimum_required(VERSION 3.0.0)
project(reding_img VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(reading_image main.cpp)

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

target_link_libraries( reading_image ${OpenCV_LIBS} )
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

