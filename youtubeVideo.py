# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 02:36:33 2024

@author: gksac
"""

import cv2 
import pafy

url="https://www.youtube.com/watch?v=Uhoqjp-3LTQ&ab_channel=BnfTV"
data=pafy.new(url)
capture= cv2.VideoCapture(0)
data= data.getbestvideo(preftype="mp4")
capture.open(data.url)
print("check==",capture.isOpened())
"""
Youtube video 
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
        
        key=cv2.waitKey(25)
        if cv2.waitKey(1) & key == ord("q"):
           break 
        
capture.release()
output.release()