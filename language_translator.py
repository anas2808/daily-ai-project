import requests
import json

class LanguageTranslator:
    """
    LanguageTranslator uses an external translation service to translate text
    from one language to another.
    """

    def __init__(self, api_key: str):
        """
        Initializes the LanguageTranslator with the given API key.
        
        :param api_key: A valid API key for the translation service.
        """
        self.api_key = api_key
        self.api_url = "https://api.cognitive.microsofttranslator.com/translate"
        self.api_version = "3.0"

    def translate_text(self, text: str, from_lang: str, to_lang: str) -> str:
        """
        Translates the given text from the source language to the target language.

        :param text: The text to translate.
        :param from_lang: The language code of the source language (e.g., 'en').
        :param to_lang: The language code of the target language (e.g., 'es').
        :return: The translated text.
        :raises ValueError: If the translation fails.
        """
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Content-type': 'application/json',
            'Ocp-Apim-Subscription-Region': 'global'
        }
        
        params = {
            'api-version': self.api_version,
            'from': from_lang,
            'to': to_lang
        }
        
        body = [{
            'text': text
        }]
        
        response = requests.post(self.api_url, headers=headers, params=params, json=body)
        
        if response.status_code != 200:
            raise ValueError(f"Translation failed with status code {response.status_code}: {response.text}")
        
        try:
            translation_result = response.json()
            translated_text = translation_result[0]['translations'][0]['text']
            return translated_text
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            raise ValueError("Failed to parse translation response") from e

def main():
    # Example usage of the LanguageTranslator class
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    translator = LanguageTranslator(api_key)

    text_to_translate = "Hello, world!"
    source_language = "en"
    target_language = "es"

    try:
        translated_text = translator.translate_text(text_to_translate, source_language, target_language)
        print(f"Translated Text: {translated_text}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()