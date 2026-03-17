cmake_minimum_required(VERSION 3.0.2)
project(vehicle_detection)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  std_msgs
  cv_bridge
)

catkin_package()

# 安裝 Python 腳本，使其在 ROS 環境中可執行
catkin_install_python(PROGRAMS
  scripts/detect_cars.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
