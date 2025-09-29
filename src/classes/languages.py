class LanguageConverter:
  EASYOCR_TO_GOOGLE = {
    # Only include languages supported by both EasyOCR and Google Translate.
    "af": "af",  # Afrikaans
    "ar": "ar",  # Arabic
    "az": "az",  # Azerbaijani
    "be": "be",  # Belarusian
    "bg": "bg",  # Bulgarian
    "bn": "bn",  # Bengali
    "bs": "bs",  # Bosnian
    "ch_sim": "zh-CN",  # Simplified Chinese
    "ch_tra": "zh-TW",  # Traditional Chinese
    "cs": "cs",  # Czech
    "cy": "cy",  # Welsh
    "da": "da",  # Danish
    "de": "de",  # German
    "en": "en",  # English
    "es": "es",  # Spanish
    "et": "et",  # Estonian
    "fa": "fa",  # Persian (Farsi)
    "fr": "fr",  # French
    "ga": "ga",  # Irish
    "hi": "hi",  # Hindi
    "hr": "hr",  # Croatian
    "hu": "hu",  # Hungarian
    "id": "id",  # Indonesian
    "is": "is",  # Icelandic
    "it": "it",  # Italian
    "ja": "ja",  # Japanese
    "kn": "kn",  # Kannada
    "ko": "ko",  # Korean
    "ku": "ku",  # Kurdish
    "la": "la",  # Latin
    "lt": "lt",  # Lithuanian
    "lv": "lv",  # Latvian
    "mi": "mi",  # Maori
    "mn": "mn",  # Mongolian
    "mr": "mr",  # Marathi
    "ms": "ms",  # Malay
    "mt": "mt",  # Maltese
    "ne": "ne",  # Nepali
    "nl": "nl",  # Dutch
    "no": "no",  # Norwegian
    "pl": "pl",  # Polish
    "pt": "pt",  # Portuguese
    "ro": "ro",  # Romanian
    "ru": "ru",  # Russian
    "rs_cyrillic": "sr",  # Serbian (cyrillic)
    "rs_latin": "sr",  # Serbian (latin)
    "sk": "sk",  # Slovak
    "sl": "sl",  # Slovenian
    "sq": "sq",  # Albanian
    "sv": "sv",  # Swedish
    "sw": "sw",  # Swahili
    "ta": "ta",  # Tamil
    "te": "te",  # Telugu
    "th": "th",  # Thai
    "tjk": "tg",  # Tajik
    "tl": "tl",  # Tagalog
    "tr": "tr",  # Turkish
    "ug": "ug",  # Uyghur
    "uk": "uk",  # Ukranian
    "ur": "ur",  # Urdu
    "uz": "uz",  # Uzbek
    "vi": "vi",  # Vietnamese
  }

  def easyocr_to_google(self, easyocr_code):
    return self.EASYOCR_TO_GOOGLE.get(easyocr_code)