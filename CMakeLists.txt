cmake_minimum_required(VERSION 2.8.3)
project(autonomous_ship)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
)
catkin_package(
  INCLUDE_DIRS
  include
  LIBRARIES autonomous_ship
  CATKIN_DEPENDS message_generation roscpp rospy std_msgs
  )

include_directories(
  INCLUDE_DIRS
  include
  ${catkin_INCLUDE_DIRS}
)

