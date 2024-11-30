# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:07:28 2024

@author: k-ruko
"""

#dengan open cv
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/k-ruko/Downloads/sucipto.jfif")
cv2.resize(200,40)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)


magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitimshude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

#dengan numpy
#