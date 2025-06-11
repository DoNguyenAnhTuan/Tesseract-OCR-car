import cv2
import numpy as np

#######   training part    ############### 
samples = np.loadtxt('MauThuVien.data',np.float32)
responses = np.loadtxt('PhanHoi.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.ml.KNearest_create()
#model.train(samples,responses)
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

############################# testing part  #########################

im = cv2.imread('1234.png') #phân tích ảnh đầu vào thành pixel
out = np.zeros(im.shape,np.uint8) #tạo ma trận 0 với kích thước bằng im, kiểu là unsigned int
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #chuyển ảnh đầu vào thành đen trắng
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2) #chuyển ảnh về nhị phân

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>20:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2) #vẽ hình đầu vào, bao bọc những con số đã được nhận dạng
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
            string = str(int((results[0][0]))) #danh sách những con số đã được nhận dạng
            cv2.putText(out,string,(x,y+h),0,1,(0,255,0)) #vẽ hình đầu ra từ những con số đó

cv2.imshow('Input',im)
cv2.imshow('Output',out)
cv2.waitKey(0)
