# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:42:03 2024

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:29:06 2024

@author: Lenovo
"""

import cv2
import numpy as np

# Membaca citra grayscale
img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\pryg.jpg'', 100)

# Deteksi tepi menggunakan Canny
canny = cv2.Canny(img, 100, 200)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
