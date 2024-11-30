# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:33:04 2024

@author: user
"""

import numpy as np
import cv2

cam = cv2.VideoCapture("C:\\Users\\user\\Videos\\Screen Recordings\\Screen Recording 2024-09-17 102239.mp4", 0 )

#konvolusi manual
def konvolusi(image, kernel):
    row,col= image.shape
    mrow,mcol=kernel.shape
    h =int(mrow/2)

    canvas = np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or i==row-1 or j==col-1:
                canvas.itemset((i,j),0)
            else:
                imgsum=0
                for k in range (-h, mrow-h):
                    for l in range (-h, mcol-h):
                        res=image[i+k,j+l] * kernel[h+k,h+l]
                        imgsum+=res
                    canvas.itemset((i,j), imgsum)
    return canvas
 
def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)
    canvas = konvolusi(image, kernel)
    return canvas

def kernel2(image):
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
    canvas2 = konvolusi(image, kernel)
    return canvas2

while True: 
    #mengubah masing masing citra sesuai dengan perintahnya
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    test1=kernel1(gray)
    cv2.imshow("gambar1",gray)
    cv2.imshow("High pass",test1)

    test2=kernel2(gray)
    cv2.imshow("gambar2",gray)
    cv2.imshow("low pass",test2)

    print(" gamabr1 ", gray)    
    print(" gambar2 ", gray)
    print(" gambar1 ", gray.shape)
    print(" gambar2 ", gray.shape) 
    print(" high filter image1 ", test1.shape)
    print(" lowpass image1", test1.shape)
    print(" high filter image2 ", test2.shape)
    print(" lowpass image2", test2.shape)
    
    if cv2.waitKey(1)==ord('1'):
        break
cv2.destroyAllWindows()

"""

  Operating System: Windows 11 Home Single Language 64-bit (10.0, Build 22631) (22621.ni_release.220506-1250)
                 Language: English (Regional Setting: English)
      System Manufacturer: LENOVO
             System Model: 82KT
                     BIOS: GLCN48WW (type: UEFI)
                Processor: AMD Ryzen 3 5300U with Radeon Graphics          (8 CPUs), ~2.6GHz
                   Memory: 8192MB RAM
      Available OS Memory: 5990MB RAM
                Page File: 8703MB used, 5989MB available
              Windows Dir: C:\WINDOWS
          DirectX Version: DirectX 12

          
         """