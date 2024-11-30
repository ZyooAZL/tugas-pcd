import numpy as np
import cv2

# Membaca gambar dalam mode grayscale
image1 = cv2.imread("c:\Users\user\Pictures\Camera Roll\WIN_20230911_13_26_29_Pro.jpg",0)
image2 = cv2.imread("c:\Users\user\Pictures\Camera Roll\WIN_20230911_13_26_29_Pro.jpg",0)

# Fungsi konvolusi manual
def konvolusi(image, kernel):
    row, col = image.shape
    mrow, mcol = kernel.shape
    h = mrow // 2

    # Menambahkan padding pada gambar
    padded_image = np.pad(image, ((h, h), (h, h)), mode='constant', constant_values=0)
    canvas = np.zeros((row, col), np.float32)
    
    for i in range(row):
        for j in range(col):
            region = padded_image[i:i+mrow, j:j+mcol]
            canvas[i, j] = np.sum(region * kernel)
    
    # Mengembalikan hasil konvolusi dalam rentang 0-255
    canvas = np.clip(canvas, 0, 255).astype(np.uint8)
    return canvas

# Fungsi untuk kernel high pass
def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9], [-1/9, 8/9, -1/9], [-1/9, -1/9, -1/9]], np.float32)
    canvas = konvolusi(image, kernel)
    return canvas

# Fungsi untuk kernel low pass
def kernel2(image):
    kernel = np.array([[0, 1/8, 0], [1/8, 1/2, 1/8], [0, 1/8, 0]], np.float32)
    canvas2 = konvolusi(image, kernel)
    return canvas2

# Mengaplikasikan kernel pada gambar
test1 = kernel1(image1)
test2 = kernel2(image2)

# Menampilkan hasil
cv2.imshow("gambar1", image1)
cv2.imshow("High pass", test1)
cv2.imshow("gambar2", image2)
cv2.imshow("Low pass", test2)
cv2.waitKey(0)
cv2.destroyAllWindows()