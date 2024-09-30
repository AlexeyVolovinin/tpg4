from deep_translator import GoogleTranslator
# !pip install deep_translator
# Text to be translated
text_to_translate = """
Привет, как дела?
"""

# Translate the text to Spanish
translated_text = GoogleTranslator(source='auto', target='en').translate(text_to_translate)

print(f"Translated text: {translated_text}")
