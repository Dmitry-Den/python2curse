import pytesseract
import os
from PIL import Image

img = Image.open('Screenshot_2.jpg')
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   

file_name = img.filename
filename = file_name.split('.')[0]

custom_config = r'--oem 3 --psm 13'

text = pytesseract.image_to_string(img, custom_config)
print(text)

with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)