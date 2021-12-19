cmake_minimum_required(VERSION 3.0.0)
project(crop_region VERSION 0.1.0)

include(CTest)
enable_testing()
find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)
include_directories(OpenCV_INCLUDS_DIRS)
add_executable(crop_region main.cpp)
target_link_libraries(crop_region ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
