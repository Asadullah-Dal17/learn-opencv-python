cmake_minimum_required(VERSION 3.0.0)
project(seting_pixel_values VERSION 0.1.0)

include(CTest)
enable_testing()
find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)
add_executable(setting_pixel_values main.cpp)
# linking the libraries 
include_directories(${OpenCV_INCLUDES_DIRS})
target_link_libraries(setting_pixel_values ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

