import cv2                     # Mengimpor pustaka OpenCV untuk pemrosesan citra
import numpy as np             # Mengimpor pustaka NumPy untuk operasi numerik

def calculate_mse(original, distorted):
    """
    Fungsi untuk menghitung Mean Square Error (MSE) antara citra asli dan citra yang terdistorsi.
    MSE dihitung dengan mengambil rata-rata kuadrat selisih antara dua citra.
    """
    # Menghitung selisih antara citra asli dan citra yang terdistorsi
    err = np.sum((original.astype("float") - distorted.astype("float")) ** 2)
    
    # Menghitung MSE dengan membagi total kesalahan dengan jumlah pixel
    mse = err / float(original.shape[0] * original.shape[1])
    
    return mse                    # Mengembalikan nilai MSE

def calculate_psnr(original, distorted):
    """
    Fungsi untuk menghitung Peak Signal-to-Noise Ratio (PSNR).
    PSNR dihitung berdasarkan nilai MSE.
    """
    mse = calculate_mse(original, distorted)  # Menghitung MSE terlebih dahulu
    if mse == 0:                              # Jika MSE adalah 0, artinya kedua citra identik
        return float("inf")                   # Kembalikan tak hingga sebagai PSNR

    # Menghitung PSNR menggunakan rumus
    psnr = 10 * np.log10(255 ** 2 / mse)     
    
    return psnr                                # Mengembalikan nilai PSNR

# Membaca citra asli dan citra terdistorsi dari file
original_image = cv2.imread('C:/Users/user/Pictures/download.jpeg')  # Mengimpor citra asli
distorted_image = cv2.imread('C:/Users/user/Pictures/download.jpeg') # Mengimpor citra yang terdistorsi

# Menghitung MSE dan PSNR
mse_value = calculate_mse(original_image, distorted_image)    # Menghitung MSE
psnr_value = calculate_psnr(original_image, distorted_image)  # Menghitung PSNR

# Menampilkan hasil
print(f'Mean Square Error (MSE): {mse_value}')  # Mencetak nilai MSE
print(f'Peak Signal-to-Noise Ratio (PSNR): {psnr_value} dB')  # Mencetak nilai PSNR