import fitz
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)

    full_text = ""

    for page in doc:

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        img = Image.open(io.BytesIO(pix.tobytes("png")))

        text = pytesseract.image_to_string(img)

        full_text += text + "\n"

    return full_text