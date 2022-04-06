import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Programme\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("./bilder/plan_link1.jpg")


text = pytesseract.image_to_string(img)

file = open("./text.txt", "w", encoding="utf8")
file.write(text)
file.close()

print(text)

