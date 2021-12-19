cmake_minimum_required(VERSION 3.0.0)
project(empty_image VERSION 0.1.0)

include(CTest)
enable_testing()
find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)
add_executable(empty_image main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
