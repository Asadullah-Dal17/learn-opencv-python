cmake_minimum_required(VERSION 3.0.0)
project(blruring_Region VERSION 0.1.0)

include(CTest)
enable_testing()
find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)
add_executable(blurring_region main.cpp)
include_directories(${OpenCV_INCLUDS_DIRS})
target_link_libraries(blurring_region ${OpenCV_LIBS} )

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
