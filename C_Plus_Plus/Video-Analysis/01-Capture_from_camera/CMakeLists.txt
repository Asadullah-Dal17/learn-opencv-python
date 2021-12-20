cmake_minimum_required(VERSION 3.0.0)
project(Camera_Capture VERSION 0.1.0)

include(CTest)
enable_testing()
find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)

add_executable(Camera_Capture main.cpp)
include_directories(${OpenCV_INCLUDS_DIRS})
target_link_libraries(Camera_Capture ${OpenCV_LIBS} )
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
