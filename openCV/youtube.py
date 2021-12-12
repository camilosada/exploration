from cv2 import cv2


"""
resized=cv2.resize(img,(int(img.shape[1]/2) , int(img.shape[1]/2)))
cv2.imshow("resized",resized)
print(img.shape)
cv2.waitKey()


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
"""
img=cv2.imread('pface2.jpg')
cv2.imshow("gg",img) 
"""
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(100,0,150),1)
    
cv2.imshow("gg",img)    
"""
cv2.waitKey(0)