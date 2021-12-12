from cv2 import cv2
import time
import pandas as pd
from datetime import datetime

#face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
first_frame = None
status_list=[None,None]
times=[]
df=pd.DataFrame(columns=["start","end"])


video=cv2.VideoCapture(0)

a=1

while True:

    a=a+1
    check,frame= video.read() #frame: primer imagen del video, check: python puede leer la cam?
    status=0
    gray_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame= cv2.GaussianBlur(gray_frame,(21,21),0)

    if first_frame is None:
        first_frame=gray_frame
        continue


    
    #faces=face_cascade.detectMultiScale(gray_frame,scaleFactor=1.08, minNeighbors=5)

    delta_frame=cv2.absdiff(first_frame,gray_frame)
    thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta,None, iterations=0)
    
    cnts,pp=cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)


    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    status_list.append(status)
    status_list=status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())    
  
  # for x,y,w,h in faces:
    #    gray_frame=cv2.rectangle(gray_frame,(x,y),(x+w,y+h),(100,0,150),1)

    cv2.imshow('grey',gray_frame)
    cv2.imshow('delta binario',thresh_delta)
    cv2.imshow('capvideo',frame)
    cv2.imshow('delta',delta_frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

    
for i in range (0,len(times),2):
    df=df.append({"start":times[i],"end":times[i+1]},ignore_index=True)

#archivo= open("time.cvs","w")
df.to_csv("time.cvs")    
print(check)
print(a)

video.release()
cv2.destroyAllWindows