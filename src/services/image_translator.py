import easyocr
import numpy as np

from PIL import Image, ImageDraw, ImageFont
from deep_translator import GoogleTranslator
from typing import List, Tuple

from src.classes.languages import LanguageConverter

class ImageTranslator:

  def translate_image(self, image: np.ndarray, from_lang: str, to_lang: str) -> np.ndarray:
    text_boxes = self._perform_ocr(image, from_lang)
    translated_texts = self._translate_texts(text_boxes, from_lang, to_lang)
    output_image = self._replace_text_with_translation(image, translated_texts, text_boxes)
    return output_image
  
  def _perform_ocr(self, image: np.ndarray, from_lang: str) -> List[Tuple[List[List[int]], str]]:
    reader = easyocr.Reader([from_lang], model_storage_directory = "model")
    result = reader.readtext(image, width_ths=0.8,  decoder="wordbeamsearch")
    extracted_text_boxes = [(entry[0], entry[1]) for entry in result if entry[2] > 0.4]
    return extracted_text_boxes

  def _translate_texts(self, text_boxes: List[Tuple[List[List[int]], str]], from_lang: str, to_lang: str) -> List[str]:
    language_converter = LanguageConverter()
    google_from_lang = language_converter.easyocr_to_google(from_lang)
    google_to_lang = language_converter.easyocr_to_google(to_lang)
    translator = GoogleTranslator(source=google_from_lang, target=google_to_lang)
    translated_texts = []
    for text_box, text in text_boxes:
      translated_texts.append(translator.translate(text))
    return translated_texts

  def _replace_text_with_translation(self, image: np.ndarray, translated_texts: List[str], text_boxes: List[Tuple[List[List[int]], str]]) -> np.ndarray:
    if isinstance(image, np.ndarray):
      image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    for text_box, translated in zip(text_boxes, translated_texts):
      if translated is None:
        continue

      x_min, y_min = text_box[0][0][0], text_box[0][0][1]
      x_max, y_max = text_box[0][0][0], text_box[0][0][1]

      for coordinate in text_box[0]:
        x, y = coordinate
        if x < x_min:
          x_min = x
        elif x > x_max:
          x_max = x
        if y < y_min:
          y_min = y
        elif y > y_max:
          y_max = y

      background_color = self._get_background_color(image, x_min, y_min, x_max, y_max)

      draw.rectangle(((x_min, y_min), (x_max, y_max)), fill=background_color)

      font, x_offset, y_offset = self._get_font(image, translated, x_max - x_min, y_max - y_min)

      draw.text(
        (x_min + x_offset, y_min + y_offset),
        translated,
        fill=self._get_text_fill_color(background_color),
        font=font,
      )

    return np.array(image)

  def _get_background_color(self, image, x_min, y_min, x_max, y_max):
    image = image.convert("RGBA")  # Handle transparency

    margin = 10
    edge_region = image.crop((
      max(x_min - margin, 0),
      max(y_min - margin, 0),
      min(x_max + margin, image.width),
      min(y_max + margin, image.height),
    ))

    pixels = list(edge_region.getdata())
    opaque_pixels = [pixel[:3] for pixel in pixels if pixel[3] > 0]

    if not opaque_pixels:
      background_color = (255, 255, 255)  # fallback if all pixels are transparent
    else:
      from collections import Counter
      most_common = Counter(opaque_pixels).most_common(1)[0][0]
      background_color = most_common

    background_color = self._add_discoloration(background_color, 40)
    return background_color

  def _add_discoloration(self, color, strength):
    r, g, b = color[:3]
    r = max(0, min(255, r + strength))
    g = max(0, min(255, g + strength))
    b = max(0, min(255, b + strength))

    if r == 255 and g == 255 and b == 255:
      r, g, b = 245, 245, 245

    return (r, g, b)

  def _get_font(self, image, text, width, height):
    # Default values at start
    font_size = None  # For font size
    font = None  # For object truetype with correct font size
    box = None  # For version 8.0.0
    x = 0
    y = 0

    draw = ImageDraw.Draw(image)  # Create a draw object

    # Test for different font sizes
    for size in range(1, 500):

      # Create new font
      new_font = ImageFont.load_default(size=font_size)

      # Calculate bbox for version 8.0.0
      new_box = draw.textbbox((0, 0), text, font=new_font)

      # Calculate width and height
      new_w = new_box[2] - new_box[0]  # Bottom - Top
      new_h = new_box[3] - new_box[1]  # Right - Left

      # If too big then exit with previous values
      if new_w > width or new_h > height:
        break

      # Set new current values as current values
      font_size = size
      font = new_font
      box = new_box
      w = new_w
      h = new_h

      # Calculate position (minus margins in box)
      x = (width - w) // 2 - box[0]  # Minus left margin
      y = (height - h) // 2 - box[1]  # Minus top margin

    return font, x, y


  def _get_text_fill_color(self, background_color):
    luminance = (
      0.299 * background_color[0]
      + 0.587 * background_color[1]
      + 0.114 * background_color[2]
    ) / 255
    if luminance > 0.5:
      return "black"
    else:
      return "white"