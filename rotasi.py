# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:42:17 2024

@author:user
"""


import cv2
import numpy as np
img = cv2.imread("C:/Users/user/Pictures/Camera Roll/WIN_20240911_08_40_12_Pro.jpg")
print(img.shape)

baris, coloms, ghgh = img.shape

#MTranslasi = np.float32([[2, 0, 100],[0, 2, 50]])

#print(MTranslasi, '\n')

MRotasi = cv2.getRotationMatrix2D((coloms/2, baris/2,),90, 1)

print(MRotasi, '\n')


dst = cv2.warpAffine (img, MRotasi, (coloms, baris))
#dst = cv2.warpAffine (img, MTranslasi, (coloms, baris))
cv2.imshow("title", dst) 
#cv2.imshow("rotasi", )

cv2.waitKey(0)
cv2.destroyAllWindows()