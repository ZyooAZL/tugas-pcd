import cv2                     # Mengimpor pustaka OpenCV untuk pemrosesan citra
import numpy as np             # Mengimpor pustaka NumPy untuk operasi numerik

def calculate_ber(image1, image2):
    """
    Fungsi untuk menghitung Bit Error Rate (BER) antara dua citra.
    BER mengukur proporsi pixel yang salah antara dua citra.
    """
    # Memastikan citra memiliki ukuran yang sama
    if image1.shape != image2.shape:  # Memeriksa apakah kedua citra memiliki ukuran yang sama
        raise ValueError("Citra harus memiliki ukuran yang sama!")  # Jika tidak, raise exception

    # Menghitung jumlah pixel yang berbeda
    difference = np.sum(image1 != image2)  # Menghitung jumlah pixel yang berbeda antara kedua citra

    # Menghitung total jumlah pixel
    total_pixels = image1.size  # Mendapatkan total jumlah pixel dari citra

    # Menghitung Bit Error Rate (BER)
    ber = difference / total_pixels  # Menghitung BER sebagai rasio pixel yang salah terhadap total pixel
    return ber                       # Mengembalikan nilai Bit Error Rate

# Membaca citra dari file
image1 = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra pertama dalam skala abu-abu
image2 = cv2.imread('image2.png', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra kedua dalam skala abu-abu

# Menghitung Bit Error Rate antara kedua citra
ber_value = calculate_ber(image1, image2)  # Memanggil fungsi untuk menghitung Bit Error Rate

# Menampilkan hasil
print(f'Bit Error Rate (BER): {ber_value}')  # Mencetak nilai Bit Error Rate ke konsol