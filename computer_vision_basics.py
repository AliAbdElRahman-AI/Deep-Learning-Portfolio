import cv2
import numpy as np

# This code demonstrates basic Image Processing for AI Computer Vision
def process_image(image_path):
    # 1. Load the image
    img = cv2.imread(image_path)
    
    if img is None:
        return "Image not found! Please check the path."

    # 2. Convert to Grayscale (Essential for many AI models)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Apply Gaussian Blur to reduce noise
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    return "Success: Image processed for AI detection."

print(process_image('test_image.jpg'))
