# -- coding: utf-8 --
"""
Created on Wed Sep 11 08:24:12 2024

@author: Lenovo
"""

'''
1.  B.  HPF, memiliki ciri-ciri kernel dari HPF adalah nilainya terdiri dari positif,nol, dan negatif,
        dan jumlah dari semua nilainya sama dengan nol. Hasilnya, edge atau tepi citra terlihat lebih tajam.
    C.  Digunakan untuk melakukan proses deteksi tepi
2.  B.  LPF, memiliki ciri-ciri semua nilainya positif dan jumlah dari semua nilainya sama dengan satu
        Low Pass Filter (LPF) mengambil komponen citra yang berfrekuensi rendah dan menahan komponen berfrekuensi tinggi
    C.  Digunakan untuk melakukan proses efek blur dan reduksi noise
'''

#G64160017
import numpy as np
import cv2



camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 340)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 680)

image1 = cv2.imread("C:/Users/user/Pictures/WLPPR/wp7203346-men-i-trust-wallpapers.jpg",0)
print(image1)
print("Ukuran Gambar:", camera.shape)
image2= cv2.imread("C:/Users/user/Pictures/WLPPR/wp7203346-men-i-trust-wallpapers.jpg",0)
print(image2)
print("Ukuran Gambar:", camera.shape)

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

test1=kernel1(camera)
cv2.imshow("gambar1",camera)
cv2.imshow("High pass",test1)
print(image1)


test2=kernel2(camera)
cv2.imshow("gambar2",camera)
cv2.imshow("low pass",test2)
print(image2)


cv2.waitKey(0)
cv2.destroyAllWindows()