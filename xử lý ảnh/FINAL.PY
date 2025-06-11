
import numpy as np 
import cv2
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

img=cv2.imread('5.png')# đọc ảnh màu
cv2.imshow('HINH ANH GOC', img)


gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #chuyển ảnh sang màu xám
thresh=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)# tạo ngương.#nhị phân hóa bức ảnh bằng cách đặt ngưỡng
contours,h = cv2.findContours(thresh, 1, 2)# tìm contour là việc tìm một đối tượng có màu trắng trên nền đen
largest_rectangle = [0,0]# giới hạn
for cnt in contours:
    approx =cv2.approxPolyDP(cnt, 0.01* cv2.arcLength(cnt,True),True)#xấp xỉ- tính chu vi approx
    if len (approx) == 4:  #có số lượng điểm bằng 4
        area=cv2.contourArea(cnt)# Tính diện tích của contour
        if area>largest_rectangle[0]:
            largest_rectangle = [cv2.contourArea(cnt), cnt, approx]
x,y,w,h = cv2.boundingRect(largest_rectangle[1])  # Tính diện tích bouding box 

image= img[y:y+h,x:x+w]
cv2.drawContours(img, [largest_rectangle[1]],0,(0,255,0),4)#màu xanh lá cây thì set là (0,255,0)-vẽ lại ảnh contour vào ảnh gốc
cropped = img[y:y+h,x:x+w]
cv2.imshow('DANH DAU DOI TUONG',img)

cv2.drawContours(img, [largest_rectangle[1]],0,(255,255,255),14)
#cv2.imshow('cach khung bien so',img)  

pytesseract.pytesseract.tesseract_cmd='C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)# chuyển ảnh màu sang dạng grayscale
blur = cv2.GaussianBlur (gray,(3,3), 0)# làm mờ ảnh
thresh = cv2.threshold (blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]#nhị phân hóa bức ảnh bằng cách đặt ngưỡng
cv2.imshow('KET QUA',thresh)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))   
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)# biến đổi hình thái học
invert = 255 - opening #đảo ngược màu
data= pytesseract.image_to_string(invert, lang='eng', config='--psm 6')#psm (Chế độ phân đoạn trang)
print("THONG TIN NHAN DIEN:")
print(data)
cv2.waitKey()


            
