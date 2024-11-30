import cv2

def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resize image to a specific width or height while maintaining aspect ratio.

    :param image: Input image.
    :param width: New width of the image (optional).
    :param height: New height of the image (optional).
    :param inter: Interpolation method (optional).
    :return: Resized image.
    """
    (h, w) = image.shape[:2]
    
    # If no dimensions provided, return the original image
    if width is None and height is None:
        return image
    
    # Calculate the aspect ratio
    if width is None:
        # Calculate width based on height
        aspect_ratio = height / float(h)
        new_dim = (int(w * aspect_ratio), height)
    elif height is None:
        # Calculate height based on width
        aspect_ratio = width / float(w)
        new_dim = (width, int(h * aspect_ratio))
    else:
        new_dim = (width, height)
    
    # Resize the image using cv2.resize
    resized_image = cv2.resize(image, new_dim, interpolation=inter)
    
    return resized_image


def add_text(image, text, position=(10, 30), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 255, 0), thickness=2):
    """
    Menambahkan teks pada gambar.

    :param image: Input image.
    :param text: Teks yang akan ditambahkan.
    :param position: Posisi teks (x, y).
    :param font: Jenis font.
    :param font_scale: Skala font.
    :param color: Warna teks dalam format (B, G, R).
    :param thickness: Ketebalan teks.
    """
    cv2.putText(image, text, position, font, font_scale, color, thickness)
