
import io
import pytesseract
from PIL import Image

def process_ocr(image_file):
    try:
        # if image_file.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
        #     return {"error": "Invalid file type"}, 400

        image = Image.open(io.BytesIO(image_file.read()))

        text = pytesseract.image_to_string(image, lang='eng')
        return {"text": text, "message": "OCR successful"}, 200
    except Exception as e:
        print("Error: ", str(e))
        return {"error": str(e)}, 500

