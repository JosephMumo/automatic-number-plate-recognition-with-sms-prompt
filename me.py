from sys import executable
import cv2 as cv
import mysql.connector
from africastalking import initialize, SMS
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract.exe"
vid=cv.VideoCapture(0)
while True:
    ret,frame=vid.read()
    ret2,frame2=vid.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (T, binarized) = cv.threshold(frame, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    

    ######################################################3
    image_h=frame.shape[0]
    image_w=frame.shape[1]
    boxes=(pytesseract.image_to_boxes(binarized))
    numplate=(pytesseract.image_to_string(binarized))
    text=''
    
    for character in boxes.splitlines():
        character=character.split(" ")
        #print(character)
        x,y,w,h=int(character[1]),int(character[2]),int(character[3]),int(character[4])
        cv.rectangle(frame2,(x,image_h-y),(w,image_h-h),(0,0,255),5)
    text+=numplate
    print(text)
    cv.imshow('frame',frame2)
######################################################3




    if cv.waitKey(1) & 0xFF==ord('q'):
        break

vid.release()
cv.destroyAllWindows()
