"""Image -> raw text extraction using Tesseract OCR."""
from io import BytesIO

import pytesseract
from PIL import Image, ImageOps

from config import TESSERACT_CMD

if TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD


def _preprocess(image: Image.Image) -> Image.Image:
    """Light preprocessing to improve OCR accuracy on label photos."""
    image = ImageOps.exif_transpose(image)  # fix phone-camera rotation
    image = image.convert("L")  # grayscale
    # Upscale small images — OCR does better on larger text
    if max(image.size) < 1200:
        scale = 1200 / max(image.size)
        new_size = (int(image.width * scale), int(image.height * scale))
        image = image.resize(new_size, Image.LANCZOS)
    return image


def extract_text(uploaded_file) -> str:
    """Run OCR on an uploaded image file-like object and return raw text.

    `uploaded_file` is whatever Streamlit's st.file_uploader returns.
    """
    image_bytes = uploaded_file.getvalue()
    image = Image.open(BytesIO(image_bytes))
    processed = _preprocess(image)
    raw_text = pytesseract.image_to_string(processed)
    return raw_text.strip()
