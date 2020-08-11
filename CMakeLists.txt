cmake_minimum_required(VERSION 2.8.3)
project(autonomous_ship)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
  message_generation
)
add_message_files(
  FILES
  imu.msg
  gps.msg
  motorValue.msg
  lidar.msg
)
generate_messages(
  DEPENDENCIES
  std_msgs
)

install(PROGRAMS
  forRasPi/imuver2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


catkin_package(
  INCLUDE_DIRS
  LIBRARIES autonomous_ship
  CATKIN_DEPENDS message_generation message_runtime roscpp rospy std_msgs
  )
include_directories(
  INCLUDE_DIRS
  include
  ${catkin_INCLUDE_DIRS}
)

