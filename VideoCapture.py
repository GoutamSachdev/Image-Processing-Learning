# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:56:25 2024

@author: gksac
"""

import cv2 
capture= cv2.VideoCapture("E:\Image-Processing-Learning\Video.mp4")
print("capture",capture)

while True:
    ret,frame=capture.read()
    frame=cv2.resize(frame,(700,450))
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video Frame",frame)
    key=cv2.waitKey(25)
    if key == ord("q"):
       break 
        
capture.release()
cv2.destroyAllWindows() 

"""
VIdeo is capturing from WEBCAM(0) use if external webcame so u have to use 
cv2.VideoCapture(1,cv2.CAP_DSHOW)
cv2.CAP_DSHOW use for previous version error of python like not compatibale 
"""

capture= cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("capture",capture)

"""
VIdeo is now saving with the help fourcc (manager which help as to write the multiple frame)

"""
#XVID ,DIVX, MJPG, X264 ,WMV1,WMV2
fourcc =cv2.VideoWriter_fourcc(*"XVID") #
#XNAME, CODEC , FPS, RESOLUTION
output=cv2.VideoWriter("E:\Image-Processing-Learning\Save.mp4",fourcc,20.0,(640,480),0)
while capture.isOpened():
    ret,frame=capture.read()
    if ret== True:
        #frame=cv2.resize(frame,(700,450)) not because already manage in writing
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow("Video Frame",frame)
        output.write(frame)
        key=cv2.waitKey(25)
        if cv2.waitKey(1) & key == ord("q"):
           break 
        
capture.release()
output.release()
    
cv2.destroyAllWindows() 