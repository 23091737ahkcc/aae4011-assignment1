#!/usr/bin/env python3
import rospy
import cv2
import torch
import numpy as np
from sensor_msgs.msg import CompressedImage

class VehicleDetector:
    def __init__(self):
        rospy.init_node('vehicle_detector', anonymous=True)
        # 加載輕量化模型以提升速度
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.image_sub = rospy.Subscriber("/hikcamera/image_2/compressed", CompressedImage, self.callback, queue_size=1)
        
        self.count = 0  # 用於跳幀計數
        self.last_annotated = None
        rospy.loginfo("流暢模式啟動：正在同步原始影像速度...")

    def callback(self, ros_data):
        try:
            # 1. 解碼影像 (維持原始解析度)
            np_arr = np.frombuffer(ros_data.data, np.uint8)
            cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if cv_image is not None:
                # 2. 跳幀邏輯：每 3 幀才跑一次 AI，減少 CPU 負擔
                if self.count % 3 == 0:
                    results = self.model(cv_image)
                    self.last_annotated = np.squeeze(results.render())
                
                # 3. 顯示影像 (如果 AI 還沒跑完，就先顯示上一幀的結果，確保不卡頓)
                display_img = self.last_annotated if self.last_annotated is not None else cv_image
                cv2.imshow("Vehicle Detection Pipeline", display_img)
                cv2.waitKey(1)
                
                self.count += 1
            
        except Exception as e:
            rospy.logerr(f"Error: {e}")

if __name__ == '__main__':
    try:
        VehicleDetector()
        rospy.spin()
    except:
        cv2.destroyAllWindows()
