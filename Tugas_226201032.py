# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:51:34 2024

@author: Lenovo
"""

import cv2  #Mengimpor modul cv2 dari OpenCV untuk mengolah video
import numpy as np  #numpy digunakan untuk operasi matriks dan array

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) #Membuka koneksi ke kamera dengan ID 0 (kamera default) menggunakan DirectShow (cv2.CAP_DSHOW) sebagai backend untuk menangkap video dari kamera.
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 680)  #Mengatur lebar frame video yang ditangkap oleh kamera sebesar 680 piksel 
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 340) #Mengatur tinggi frame video yang ditangkap oleh kamera sebesar 340 piksel

if not camera.isOpened():
    print("can't open camera")  #Mengecek apakah kamera berhasil dibuka. Jika tidak maka akan muncul pesan "can't open camera" 
    exit()  #Program akan langsung keluar secara otomatis apabila pesan camera tidak berhasil terbuka muncul
    
while True: 
    Ret, frame = camera.read()  #Memulai loop utama untuk menangkap frame video. camera.read() bertugas mengembalikan dua nilai: Ret (status pembacaan) dan frame (gambar/frame yang diambil dari kamera)
    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #Mengonversi frame warna (BGR) ke grayscale (abu-abu) menggunakan konversi warna OpenCV
    (thresh,BW) = cv2.threshold(Gray,128, 255,cv2.THRESH_BINARY)  #Menerapkan thresholding biner pada gambar grayscale. Piksel dengan nilai lebih tinggi dari 100 diubah menjadi 155, dan piksel dengan nilai lebih rendah diubah menjadi 0 (hitam). Hasilnya disimpan dalam BW (Black & White).
    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)  #Mengonversi frame warna dari BGR (Blue, Green, Red) ke HSV (Hue, Saturation, Value) menggunakan konversi warna OpenCV.
    print()
    cv2.imshow("original", frame)  #Untuk menampilkan video asli dari kamera
    cv2.imshow("Gray", Gray)  #Untuk menampilkan video grayscale (abu-abu)
    cv2.imshow("BW", BW,)  #Untuk menampilkan video hasil thresholding biner
    cv2.imshow("hsv", hsv)  #Untuk menampilkan video dalam ruang warna HSV (Hue, Saturation, Value)

    if cv2.waitKey(1)==ord('q'):  #Menunggu 1 milidetik untuk menekan tombol pada jendela video. Jika menekan tombol 'q', maka akan terjadi proses keluar dari loop dan menghentikan program/kamera video
        break
cv2.destroyAllWindows()  #Menutup semua jendela yang dibuat oleh cv2.imshow() setelah keluar dari loop