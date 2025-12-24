import os
from gtts import gTTS

# --- Automatic playback setup ---
# To enable automatic playback, you need the 'playsound' library.
# If you don't have it, run this command in your terminal:
# pip install playsound
try:
    from playsound import playsound
    playsound_available = True
except ImportError:
    playsound_available = False
    print("Warning: The 'playsound' library was not found.")
    print("Audio will be saved, but not played automatically.")
    print("To enable automatic playback, run: pip install playsound")
    print("----------------------------------------------------------")


print("\n------------------------------------------")
print("  My Awesome Text-to-Speech Converter!    ")
print("------------------------------------------")

try:
    # Get text input from the user
    user_text = input("Please enter the text you want to convert to speech: ")

    if not user_text.strip():
        print("Oops! You didn't enter any text. Please try again.")
    else:
        # Set the language (default to English).
        # You can change 'en' to 'es' for Spanish, 'fr' for French, etc.
        language = 'en'
        
        # Create the gTTS object
        # 'slow=False' makes the speech at a normal pace
        speech_object = gTTS(text=user_text, lang=language, slow=False)
        
        # Define the output filename for the audio
        audio_filename = "converted_speech.mp3"
        
        # Save the generated speech to an MP3 file
        speech_object.save(audio_filename)
        
        print(f"\nSuccess! Your text has been converted to speech.")
        print(f"The audio is saved as: '{audio_filename}' in the current directory.")
        
        # Attempt to play the audio automatically if playsound is available
        if playsound_available:
            print("\nAttempting to play the audio now...")
            playsound(audio_filename)
            print("Audio playback finished.")
        else:
            print("\nTo listen to the audio, simply open 'converted_speech.mp3' with your favorite media player.")
            print("Remember to install 'playsound' for automatic playback next time!")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("\nCommon reasons for errors:")
    print("1. No internet connection (gTTS needs it to work).")
    print("2. 'gTTS' library not installed. Make sure you run: pip install gTTS")
    print("3. Issue with the text entered or language specified.")

print("\nThank you for using my converter!")
print("------------------------------------------")