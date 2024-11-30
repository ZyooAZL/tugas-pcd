import numpy as np
import cv2
import sys, inspect, os
import argparse
import collections

cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "..", "..", "Image_Lib")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
    

# Import your utils after modifying it
import image_utils as utils

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
        
def add_text(image, text):
     cv2.putText(image, text, (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
ap = argparse.ArgumentParser("Track and blur faces in video input")
ap.add_argument("-v", "--video", help="Path to video file. Defaults to webcam video")

args = vars(ap.parse_args())
 
camera = cv2.VideoCapture(0)

calibrated = False

grabbed, frame = camera.read()
if not grabbed:
    raise ValueError("Camera read failed!")
bg = image_resize(frame, height=600).astype(np.float32)  # This will now work

while True:
    grabbed, frame = camera.read()
    if not grabbed:
        print("Camera read failed")
        break

    frame = image_resize(frame, height=600)
    height, width, channels = frame.shape

    if not calibrated:
        # Sample hand color
        add_text(frame, "Press space after covering rectangle with hand. Hit SPACE when ready")
        x, y, w, h = width / 4, height / 2, 50, 50
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Calibration", frame)
        if cv2.waitKey(2) & 0xFF == ord(' '):
            roi = frame[y:y + h, x:x + w, :]
            roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            min_value = np.amin(roi_hsv, (0, 1))
            max_value = np.amax(roi_hsv, (0, 1))
            cv2.destroyWindow("Calibration")
            calibrated = True

    else:
        cv2.accumulateWeighted(frame, bg, 0.01)
        frame ^= cv2.convertScaleAbs(bg)

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hand_mask = cv2.inRange(frame_hsv, min_value, max_value)
        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        hand_mask = cv2.erode(hand_mask, kernel, iterations=2)
        hand_mask = cv2.dilate(hand_mask, kernel, iterations=2)
        
        cv2.imshow("Hand Mask After Morphology", hand_mask)
        
        hand_mask = cv2.GaussianBlur(hand_mask, (7, 7), 0).astype(np.uint8)
        
        cv2.imshow("output", frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
