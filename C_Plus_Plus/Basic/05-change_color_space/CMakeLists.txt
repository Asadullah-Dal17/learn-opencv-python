cmake_minimum_required(VERSION 3.0.0)
project(color_space VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(color_space main.cpp)
find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
include_directories(OpenCV_INCLUDES_DIRS)
target_link_libraries(color_space ${OpenCV_LIBS})