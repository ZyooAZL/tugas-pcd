import cv2                            # Mengimpor pustaka OpenCV untuk pemrosesan citra
from skimage.metrics import structural_similarity as ssim  # Mengimpor fungsi SSIM dari skimage

def calculate_ssim(image1, image2):
    """
    Fungsi untuk menghitung Structural Similarity Index (SSIM) antara dua citra.
    SSIM mengukur kesamaan struktural antara dua citra.
    """
    # Menghitung SSIM
    ssim_value, _ = ssim(image1, image2, full=True)  # Menghitung nilai SSIM dan mendapatkan citra SSIM
    return ssim_value                                   # Mengembalikan nilai SSIM

# Membaca citra dari file
image1 = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra pertama dalam skala abu-abu
image2 = cv2.imread('image2.png', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra kedua dalam skala abu-abu

# Memastikan citra memiliki ukuran yang sama
if image1.shape != image2.shape:                           # Memeriksa apakah kedua citra memiliki ukuran yang sama
    raise ValueError("Citra harus memiliki ukuran yang sama!")  # Jika tidak, raise exception

# Menghitung SSIM antara kedua citra
ssim_value = calculate_ssim(image1, image2)               # Memanggil fungsi untuk menghitung SSIM

# Menampilkan hasil
print(f'Structural Similarity Index (SSIM): {ssim_value}')  # Mencetak nilai SSIM ke konsol