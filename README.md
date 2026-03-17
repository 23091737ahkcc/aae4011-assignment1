# AAE4011 Assignment 1 — Q3: ROS-Based Vehicle Detection from Rosbag

> **Student Name:** Yim Kai Hin | **Student ID:** 25016683D | **Date:** 15-3-2026

---

## 1. Overview

In this project, we are going to search and learn how to make a ROS based vehicle detector to identify vehicle in a rosbag. The task includes finding a workable code editor and extensions, and make the code for ros detector.

## 2. Detection Method *(Q3.1 — 2 marks)*

I have chossed YOLOv5s for this project since it balances both detect speed and accuracy while maintaining the frame rate.

## 3. Repository Structure
aae4011-assignment1
  
    ├──launch

        └── terminal 1                # roscore

        └── terminal 2                # export display

        └── terminal 3                # play rosbag

    ├──scripts
   
        └── detect_cars.py            # base code

    ├── CMakeLists.txt               # Define rules and packages

    ├── README.md                    # project document

    └── package.xml                  # declarations



## 4. Prerequisites

OS: Ubuntu 20.04.6 LTS

ROS Version: ROS Noetic

Python Version: 3.8

## 5. How to Run *(Q3.1 — 2 marks)*

1. Clone the repository

        cd ~/catkin_ws/src
        git clone https://github.com/23091737ahkcc/aae4011-assignment1

   
2. Install dependencies
   
        pip3 install torch torchvision torchaudio opencv-python numpy requests
        sudo apt-get update
        sudo apt-get install ros-noetic-compressed-image-transport ros-noetic-cv-bridge


3. Build the ROS package
   
        cd ~/catkin_ws
        catkin_make
        source devel/setup.bash
        chmod +x src/vehicle_detection/scripts/detect_cars.py


4. Place the rosbag file
   
        mkdir -p ~/catkin_ws/data

5. Launch the pipeline

        roscore

        export DISPLAY=:0
        rosrun vehicle_detection detect_cars.py

        rosbag play -l ~/catkin_ws/data/*.bag


## 6. Sample Results

### Image Extraction Summary

Total frame: 1142

Resolution: 1440x1080

Topic Name: /hikcamera/image_2/compressed

### Detection Results

Sample Screenshot:<img width="1272" height="679" alt="螢幕擷取畫面 2026-03-17 012507" src="https://github.com/user-attachments/assets/25b2488d-a883-43bc-820b-ed6bf692f73d" />





## 7. Video Demonstration *(Q3.2 — 5 marks)*

**Video Link:** [YouTube (Unlisted)](https://youtu.be/zGS8g_tCuWs)

## 8. Reflection & Critical Analysis *(Q3.3 — 8 marks, 300–500 words)*

### (a) What Did You Learn? *(2 marks)*

*Identify at least two specific technical skills or concepts you gained.*


### (b) How Did You Use AI Tools? *(2 marks)*

*Describe how you used AI assistants. Discuss both benefits and limitations. If you did not use any, explain your alternative approach.*

### (c) How to Improve Accuracy? *(2 marks)*

*Propose two concrete strategies to improve detection accuracy and explain why each would help.*

### (d) Real-World Challenges *(2 marks)*

*Discuss two challenges of deploying this pipeline on an actual drone in real time.*

