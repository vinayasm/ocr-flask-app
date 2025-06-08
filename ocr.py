import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\vinay\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

image = cv2.imread('image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
pil_img = Image.fromarray(gray)
text = pytesseract.image_to_string(pil_img)

print("Extracted Text:")
print(text)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)