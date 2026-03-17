# AAE4011 Assignment 1 — Q3: ROS-Based Vehicle Detection from Rosbag

> **Student Name:** Yim Kai Hin | **Student ID:** 25016683D | **Date:** 15-3-2026

---

## 1. Overview

In this project, we are going to research and learn how to make a ROS based vehicle detector to identify vehicle in a rosbag. The task includes finding a workable code editor and extensions, and make the code for ros detector.

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

After this project, I learnt how to use ROS and optimization. For ROS, I learnt how to download and connect with the code editor. For optimization, I learnt to cut down the detection video quality during to test to ensure the scripts working. After the result is stable, I adjust the quality to balance both detection accuracy and video quality.

### (b) How Did You Use AI Tools? *(2 marks)*

I have used AI Tools for writing the Python script and terminals command.

For the benefits, it can be a teacher to teach me all the procedures from downloading a workable code editor to complete the assignment requirements with a workable vehicle detector. It also explains cleanly for every procedure and provides real time solutions when error appears.

For the limitations, it does not actually look on your screen so there will be misunderstandings during the process. Therefore, it requires users to provide detailed prompt, error information, or some screenshot for better communication and understanding.

### (c) How to Improve Accuracy? *(2 marks)*

There are two way to improve accuracy and performance, using related data and giving vehicle label.

For using related data, it can improve the detection accuracy by providing serval specific domain data like different car types data. In this project, the dataset is not corresponding and lead to wrong detection occurs.

For giving ID label, it can improve analysis by giving every vehicles an lifetime ID. Deep SORT can be a tool to give ID and improve tracting on moving cars.


### (d) Real-World Challenges *(2 marks)*

There will be challenges for real life usage, hardware and environment.

For hardware, the requirment of GPU or TPU will be higher for real time collecting data. Therefore, the high load and battery drain would also be a problem to slove.

For environment, the light conditions, shadows, and movement burr would be a problem for drone to collect data. It requires model to handle low visibility conditions.


