""" Tesseract w/ Pillow """

# from pytesseract import pytesseract
# from PIL import Image

# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# image_path = r"sample_image.png"
# image = Image.open(image_path)

# text = pytesseract.image_to_string(image)

# print(text)


""" Tesseract w/ OpenCV """

import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = r"sample_image.png"

with open(img_path, 'rb') as f:
    img = cv2.imdecode(np.frombuffer(f.read(), np.uint8), cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(
    gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

# Creating a text file to write the output to
with open("result.txt", "w+") as file:
    file.write("")

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]

    with open("result.txt", "a") as file:
        text = pytesseract.image_to_string(cropped)
        file.write(text + "\n")
