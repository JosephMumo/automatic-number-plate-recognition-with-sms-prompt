from re import U
from typing import Collection
from numpy import number, rint
import pytesseract
import cv2 as cv
import matplotlib.pyplot as plt
import mysql.connector
import  africastalking
import numpy as np
######################### SMS API######################################
username = "leonTech"    # use 'sandbox' for development in the test environment
api_key = "8f45052f9c7c74c52b721f1378b56e69c4b4e8b4d7ec95da578f711e0e4508f5"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)
sms=africastalking.SMS
################################################################

###################DATABASE CONNECTION##########################
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")
cursor = conn.cursor(buffered=True)
#############################################################################3
pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract.exe"
img_path = "numplate4.jpg"
image = cv.imread(img_path)
text=pytesseract.image_to_string(image)
collected_data=text.split("))")
for x in  collected_data:
    print(collected_data,"hello")
#################################################################################

cursor.execute("SELECT * FROM users")
"""

for x in cursor:   
    for n in x:
        for word in collected_data:
            print(word,"mearr")
            print(collected_data)
            l = str(n).find(word)
            print(n,word,"martin")
                       
            if l == 0:
                
                
               # print(l,word)
                
                cursor.execute("SELECT * FROM users WHERE numberPlate LIKE '%{}%' LIMIT 1".format(n))
                for i in cursor:
                    print("+254{}".format(i[1]))
                    print("HELLO")
                    response = africastalking.sms.send("hello world","+254{}".format(i[1])) 
                    print("SENND")




"""







#######################################################################################

img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("original ", img)
(T, binarized) = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
#cv.imshow("binarized", binarized)
######################################################################
text=pytesseract.image_to_string(binarized)
collected_data=text.split()


#cursor.execute("CREATE DATABASE test")
#cursor.execute("CREATE TABLE users(username VARCHAR(100) NOT NULL,phone INT(20) NOT NULL,email VARCHAR(100) NOT NULL,numberPlate VARCHAR(100) NOT NULL)")
#cursor.execute("INSERT INTO users(username,phone,email,numberPlate) VALUES('martin','0704332546','martin@gmail.com','BE')")
###################try######################
image_h=img.shape[0]
image_w=img.shape[1]
boxes=(pytesseract.image_to_boxes(img))
for character in boxes.splitlines():
    character=character.split(" ")
    x,y,w,h=int(character[1]),int(character[2]),int(character[3]),int(character[4])
    cv.rectangle(image,(x,image_h-y),(w,image_h-h),(0,0,255),5)



cv.imshow("mywindow",image)
###############################################
conn.commit()
cursor.execute("SELECT * FROM users")
for x in cursor:   
    for n in x:  
        for x in collected_data:
            cursor.execute("SELECT * FROM users WHERE numberPlate LIKE '%{}%' LIMIT 1".format(x))
            for y in cursor:               
                number="+254{}".format(y[1])
                user=y[0]
                    
        
            
#print(str(number))
mymsg="Hello {},\nThis is to inform you that your motor vehicle is leaving parking.\nThank you".format(user)
sms.send(mymsg,[number])                    
                
"""






l = str(n).find(word)
print(l)
    
if l == -1:


print(l,word)

cursor.execute("SELECT * FROM users WHERE numberPlate LIKE '%{}%' LIMIT 1".format(n))
for i in cursor:

response =sms.send("hello world","+254{}".format(i[1]))  
print("SEND")                                    """  


######################################################################
canny = cv.Canny(binarized, 50, 170)
lines = cv.HoughLinesP(canny, 1, np.pi / 180, 60, np.array([]), 50, 5)
# iterate over the output lines and draw them
for line in lines:
    for x1, y1, x2, y2 in line:
        cv.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv.line(canny, (x1, y1), (x2, y2), (255, 0, 0), 3)
cv.imshow("now",canny)




#cv.imshow("cany", canny)
######################################################################
text=pytesseract.image_to_string(canny)
#print(text)
######################################################################
(contours, hierarchy) = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
copiedImage = img.copy()
cv.drawContours(copiedImage, contours, -1, (0, 255, 0), 2)
cv.imshow("Contours", copiedImage)
######################################################################
text=pytesseract.image_to_string(copiedImage)
print(text.split())




######################################################################

cv.waitKey(0)
#boxesboxes=pytesseract.image_to_boxes(img)
#img_h,img_w,_=img.shape
#for boxes in boxesboxes.splitlines():
 #   boxes=boxes.split(' ')
  #  x,y,w,h=int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
   # cv.rectangle(img,(x,img_h-y),(w,img_w-h),(0,0,255),3)
#print(boxes)
#plt.imshow("leon",img)
#cv.waitKey(0)

