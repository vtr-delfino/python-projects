from PIL import Image
import glob
import os
import pytesseract

outDir = ""
cnt = 0

for img in glob.glob("C:\\Users\Vitor Delfino\Downloads\BMP\índice.bmp"):
    Image.open(img).save(os.path.join(outDir, str(cnt) + ".png"))
    cnt += 1

pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\Vitor Delfino\\Documents\\GitHub\\python-projects"

