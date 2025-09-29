import easyocr
import numpy as np
import cv2

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import Response
from src.services.image_translator import ImageTranslator

router = APIRouter(
  prefix="/translate"
)

@router.post("/image/{from_lang}/{to_lang}")
async def image(from_lang: str, to_lang: str, file: UploadFile = File(...)):
  image_translator = ImageTranslator()
  contents = await file.read()
  np_arr = np.frombuffer(contents, np.uint8)
  image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
  output = image_translator.translate_image(image, from_lang, to_lang)
  if file.content_type == "image/png":
    ret, buf = cv2.imencode('.png', output)
    media_type = "image/png"
  else:
    ret, buf = cv2.imencode('.jpg', output)
    media_type = "image/jpeg"
  return Response(content=buf.tobytes(), media_type=media_type)