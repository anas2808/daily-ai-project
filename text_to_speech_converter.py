import pyttsx3

def initialize_tts_engine():
    """
    Initializes the text-to-speech engine with default properties.
    
    Returns:
        engine: The initialized pyttsx3 engine instance.
    """
    try:
        engine = pyttsx3.init()
        # Set properties: voice rate and volume
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1.0)  # Volume 0.0 to 1.0
        return engine
    except Exception as e:
        print(f"Error initializing TTS engine: {e}")
        return None

def convert_text_to_speech(engine, text):
    """
    Converts the provided text to speech using the specified TTS engine.

    Args:
        engine: The pyttsx3 engine instance.
        text (str): The text to convert to speech.
    """
    if engine is None:
        print("TTS engine is not initialized.")
        return
    
    if not text:
        print("No text provided for conversion.")
        return

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error converting text to speech: {e}")

def main():
    """
    The main function to execute the text-to-speech conversion.
    """
    engine = initialize_tts_engine()
    user_text = input("Enter the text you want to convert to speech: ")
    convert_text_to_speech(engine, user_text)

if __name__ == "__main__":
    main()