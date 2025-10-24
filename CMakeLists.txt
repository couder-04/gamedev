cmake_minimum_required(VERSION 3.15)
project (TowerDefense CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SDL2 REQUIRED)
include_directories(${SDL2_INCLUDE_DIRS} include)

add_executable(TD src/main.cpp)
target_link_libraries(TD ${SDL2_LIBRARIES} SDL2::SDL2main)

