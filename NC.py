import cv2                     # Mengimpor pustaka OpenCV untuk pemrosesan citra
import numpy as np             # Mengimpor pustaka NumPy untuk operasi numerik

def calculate_normalized_correlation(image1, image2):
    """
    Fungsi untuk menghitung Normalized Correlation (NC) antara dua citra.
    NC mengukur tingkat kesamaan antara dua citra.
    """
    # Menghitung rata-rata dari kedua citra
    mean1 = np.mean(image1)          # Menghitung rata-rata pixel dari citra pertama
    mean2 = np.mean(image2)          # Menghitung rata-rata pixel dari citra kedua

    # Menghitung deviasi standar dari kedua citra
    std1 = np.std(image1)            # Menghitung deviasi standar pixel dari citra pertama
    std2 = np.std(image2)            # Menghitung deviasi standar pixel dari citra kedua

    # Menghitung Normalized Correlation
    correlation = np.sum((image1 - mean1) * (image2 - mean2)) / (std1 * std2 * image1.size)
    return correlation                # Mengembalikan nilai Normalized Correlation

# Membaca citra dari file
image1 = cv2.imread('C:/Users/ejaau/OneDrive/Gambar/Rol Kamera/WIN_20241120_08_35_08_Pro.jpg', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra pertama dalam skala abu-abu
image2 = cv2.imread('C:/Users/ejaau/OneDrive/Gambar/Rol Kamera/WIN_20241101_14_46_59_Pro.jpg', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra kedua dalam skala abu-abu

#menampilkan gambar
cv2.imshow("Gambar 1 (asli)", image1)
cv2.imshow("Gambar 2 (Dengan Noise)", image2)

# Memastikan citra memiliki ukuran yang sama
if image1.shape != image2.shape:                          # Memeriksa apakah kedua citra memiliki ukuran yang sama
    raise ValueError("Citra harus memiliki ukuran yang sama!")  # Jika tidak, raise exception

# Menghitung Normalized Correlation antara kedua citra
nc_value = calculate_normalized_correlation(image1, image2)  # Memanggil fungsi untuk menghitung Normalized Correlation

# Menampilkan hasil
print(f'Normalized Correlation (NC): {nc_value}')  # Mencetak nilai Normalized Correlation ke konsol