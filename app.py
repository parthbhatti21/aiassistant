import speech_recognition as sr
import time
import ai
from gtts import gTTS
def save_text_to_audio(text, filename):
    """Convert text to speech and save it as an audio file."""
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        ai.ai(text=text)
        filename="Hello.mp3"
        # save_text_to_audio(text, filename)
        # print(f"Audio saved as {filename}")
        # '''with open('example.txt', 'w') as file:
        #  file.write(text)

        # print("File created and text written successfully.")'''
    except sr.UnknownValueError:
        print(" Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from  Speech Recognition service; {e}")

if __name__ == "__main__":
    recognize_speech()
