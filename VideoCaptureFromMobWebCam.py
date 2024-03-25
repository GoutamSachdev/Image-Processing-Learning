# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 01:22:40 2024

@author: gksac
"""
import cv2 


camera="http://192.168.100.50:8080/video"
capture= cv2.VideoCapture(0)
capture.open(camera)
print("check==",capture.isOpened())
"""
Cam is exsing from my MObile device with help of IP webcame APPlication acces to my camera in IPaddress
VIdeo is now saving with the help fourcc (manager which help as to write the multiple frame)

"""
#XVID ,DIVX, MJPG, X264 ,WMV1,WMV2
fourcc =cv2.VideoWriter_fourcc(*"XVID") #
#XNAME, CODEC , FPS, RESOLUTION
output=cv2.VideoWriter("E:\Image-Processing-Learning\Save.mp4",fourcc,20.0,(640,480),0)
while capture.isOpened():
    ret,frame=capture.read()
    if ret== True:
        frame=cv2.resize(frame,(700,450)) #not because already manage in writing
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow("Video Frame",frame)
        output.write(frame)
        key=cv2.waitKey(25)
        if cv2.waitKey(1) & key == ord("q"):
           break 
        
capture.release()
output.release()
    