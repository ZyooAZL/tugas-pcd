# Hand Tracking

Program ini dirancang untuk mendeteksi dan melacak tangan dalam video input (biasanya melalui webcam), dan memberikan efek blur pada area yang terdeteksi. berikut adalah Langkah-Langkah dari penjelsan program tersebut.

## Import library yang diperlukan

``` python
import numpy as np
import cv2
import sys, inspect, os
import argparse
import collections
```

numpy as np: Digunakan untuk melakukan operasi numerik seperti manipulasi array, misalnya untuk pengolahan citra dan perhitungan.
cv2: Library OpenCV untuk pemrosesan gambar dan video, seperti membaca video, mengubah ukuran gambar, dan mengaplikasikan filter.
sys, inspect, os: Digunakan untuk operasi sistem seperti mengelola jalur file atau mengakses informasi terkait file skrip yang sedang berjalan.
argparse: Digunakan untuk menangani argumen yang diberikan oleh pengguna melalui baris perintah (misalnya untuk menentukan jalur file video).
collections: Meskipun tidak digunakan dalam program ini, biasanya digunakan untuk koleksi data yang lebih kompleks, seperti Counter, deque, dll.

## Mengatur jalur untuk library eksternal

``` python
cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "..", "..", "Image_Lib")))

if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
```

Bagian ini mencari folder Image_Lib yang terletak dua tingkat di atas skrip yang sedang dijalankan.
inspect.getfile(inspect.currentframe()) mendapatkan jalur file dari skrip yang sedang berjalan.
sys.path.insert(0, cmd_subfolder) memastikan bahwa folder Image_Lib dimasukkan ke dalam jalur Python, sehingga dapat digunakan untuk mengimpor fungsi atau kelas dari file di dalam folder tersebut.

## Improt utilitas gambar costum
``` python
import image_utils as utils
```

Setelah menambahkan Image_Lib ke jalur, program mengimpor fungsi atau kelas dari modul image_utils yang ada di folder tersebut. Fungsi atau kelas ini kemungkinan besar digunakan untuk pemrosesan gambar lebih lanjut.

## Definisi Fungsi image_resize
``` python
def image_resize(image, width=-1, height=-1):
    shape = image.shape
    if width == -1:
        if height == -1:
            return image
        else:
            return cv2.resize(image, (int(height * shape[1] / shape[0]), height))
    elif height == -1:
        return cv2.resize(image, (width, int(width * shape[0] / shape[1])))
    else:
        cv2.resize(image, (width, height))
```

Fungsi ini digunakan untuk mengubah ukuran gambar (image).
Parameter:
width: Lebar baru gambar yang diinginkan. Jika tidak ditentukan (nilai default -1), maka akan dihitung berdasarkan tinggi.
height: Tinggi baru gambar yang diinginkan. Jika tidak ditentukan (nilai default -1), maka akan dihitung berdasarkan lebar.
Jika baik lebar maupun tinggi tidak diberikan (kedua nilai adalah -1), gambar asli akan dikembalikan.
Jika salah satu nilai diberikan, maka rasio aspek gambar dipertahankan saat mengubah ukuran gambar.

## Definisi Fungsi add_text
``` python
def add_text(image, text):
     cv2.putText(image, text, (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
``` 

### Fungsi ini menambahkan teks pada gambar.
Parameter:
image: Gambar tempat teks akan ditambahkan.
text: Teks yang akan ditambahkan pada gambar.
Teks ditambahkan pada posisi (15, 15) dengan font FONT_HERSHEY_SIMPLEX, ukuran font 0.6, warna merah (0, 0, 255), dan ketebalan garis 2.

## Mengatur Argumen Baris Perintah

``` python
ap = argparse.ArgumentParser("Track and blur faces in video input")
ap.add_argument("-v", "--video", help="Path to video file. Defaults to webcam video")
args = vars(ap.parse_args())
``` 

argparse.ArgumentParser: Membuat objek parser untuk menangani argumen dari baris perintah.
ap.add_argument(...): Menambahkan argumen -v atau --video untuk menentukan jalur file video. Jika tidak ada, program akan menggunakan video dari webcam secara default.
args = vars(ap.parse_args()): Mem-parsing argumen yang diberikan dan menyimpannya dalam bentuk dictionary (args).

## Membuka Kamera

``` python
camera = cv2.VideoCapture(0)
``` 

cv2.VideoCapture(0): Membuka akses ke webcam default (indeks 0). Jika pengguna ingin menggunakan video file, mereka dapat memberikan jalur file video melalui argumen baris perintah.

## Inisialisasi Kalibrasi

``` python
calibrated = False
``` 

calibrated: Variabel boolean yang digunakan untuk menandakan apakah kalibrasi telah dilakukan. Ini digunakan untuk mengetahui apakah program sudah siap untuk mendeteksi tangan atau objek lainnya setelah kalibrasi warna.

##  Membaca Frame dan Menyusun Latar Belakang

``` python
grabbed, frame = camera.read()
if not grabbed:
    raise ValueError("Camera read failed!")
bg = image_resize(frame, height=600).astype(np.float32)
```

camera.read(): Mengambil frame pertama dari webcam.
bg = image_resize(frame, height=600): Mengubah ukuran frame pertama dengan tinggi 600 piksel, dan menjadikannya latar belakang yang akan diperbarui untuk pemisahan latar belakang.
bg.astype(np.float32): Mengkonversi tipe data gambar menjadi float32 untuk proses pemisahan latar belakang yang lebih presisi.

## Loop Pemrosesan Video

``` python
while True:
    grabbed, frame = camera.read()
    if not grabbed:
        print("Camera read failed")
        break

    frame = image_resize(frame, height=600)
    height, width, channels = frame.shape
```

Loop Utama: Program ini terus menerus menangkap frame dari video dan memprosesnya.
frame = image_resize(frame, height=600): Setiap frame yang ditangkap diubah ukurannya menjadi tinggi 600 piksel.
height, width, channels = frame.shape: Mendapatkan dimensi frame, termasuk tinggi (height), lebar (width), dan jumlah saluran warna (channels).

## Fase Kalibrasi (Mendeteksi Tangan)

``` python
if not calibrated:
    add_text(frame, "Press space after covering rectangle with hand. Hit SPACE when ready")
    x, y, w, h = width / 4, height / 2, 50, 50
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Calibration", frame)
    if cv2.waitKey(2) & 0xFF == ord(' '):
        roi = frame[y:y + h, x:x + w, :]
        roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        min_value = np.amin(roi_hsv, (0, 1))
        max_value = np.amax(roi_hsv, (0, 1))
        cv2.destroyWindow("Calibration")
        calibrated = True
```

Program menggambar kotak hijau pada posisi (x, y) untuk meminta pengguna menempatkan tangan di dalam kotak tersebut.
Setelah menekan spasi, program memilih area ROI (Region of Interest) yang berisi tangan dan mengkonversinya ke ruang warna HSV.
min_value dan max_value dihitung untuk menentukan rentang warna tangan yang digunakan untuk deteksi tangan pada frame selanjutnya.
Setelah kalibrasi, variabel calibrated diatur menjadi True.

## Pemrosesan Latar Belakang dan Deteksi Tangan

``` python
cv2.accumulateWeighted(frame, bg, 0.01)
frame ^= cv2.convertScaleAbs(bg)

frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
hand_mask = cv2.inRange(frame_hsv, min_value, max_value)

```

Pemisahan Latar Belakang: cv2.accumulateWeighted(frame, bg, 0.01) memperbarui latar belakang (model) berdasarkan frame saat ini.
frame ^= cv2.convertScaleAbs(bg): Perbedaan antara frame dan latar belakang dihitung, menghasilkan gambar yang menyoroti objek yang bergerak.
Deteksi Tangan: Mengkonversi gambar menjadi ruang warna HSV dan membuat masker tangan berdasarkan rentang warna yang telah dikalibrasi.

## Proses Morfologi pada Masker Tangan

``` python
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
hand_mask = cv2.erode(hand_mask, kernel, iterations=2

```

cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
Fungsi ini digunakan untuk membuat elemen struktural yang akan digunakan dalam operasi morfologi (dalam hal ini untuk erosi dan dilasi).
hand_mask = cv2.erode(hand_mask, kernel, iterations=2)
Fungsi cv2.erode digunakan untuk melakukan operasi erosi pada gambar atau masker biner. Operasi erosi akan mengurangi ukuran area yang berwarna putih dalam gambar biner, yang berarti area yang terdeteksi akan lebih kecil. Ini sering digunakan untuk menghilangkan noise atau memperbaiki bentuk objek.

<img width="946" alt="image" src="https://github.com/user-attachments/assets/17b968fe-d775-4caa-b8f3-82e62e784ca1">


