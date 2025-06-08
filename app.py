from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import numpy as np
import cv2
import io

app = Flask(__name__)

# Set path to Tesseract executable on your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\vinay\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename != '':
            # Read image file as bytes
            in_memory_file = io.BytesIO()
            file.save(in_memory_file)
            data = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)
            # Decode image to OpenCV format
            img = cv2.imdecode(data, cv2.IMREAD_COLOR)
            if img is not None:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # Optional: You can add preprocessing here for better OCR accuracy
                text = pytesseract.image_to_string(gray)
            else:
                text = "Error reading the image"
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
