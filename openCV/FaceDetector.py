from cv2 import cv2
import time

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
first_frame = None

video=cv2.VideoCapture(0)

a=1

while True:
    a=a+1
    check,frame= video.read() #frame: primer imagen del video, check: python puede leer la cam?
    
    gray_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray_frame,scaleFactor=1.08, minNeighbors=5)

    for x,y,w,h in faces:
        gray_frame=cv2.rectangle(gray_frame,(x,y),(x+w,y+h),(100,0,150),1)

    cv2.imshow('capvideo',gray_frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

    if first_frame is None:
        first_frame=gray_frame
        continue

print(check)
print(a)

video.release()