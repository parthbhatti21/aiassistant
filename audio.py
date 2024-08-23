from gtts import gTTS
import pygame
import os

def text_to_audio_and_play(text):
    try:
        tts = gTTS(text=text, lang='en')
        filename = "output.mp3"
        tts.save(filename)
        print(f"Audio file saved as {filename}")

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        os.remove(filename)
        print("Audio playback finished and file deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# text = "Hello, how are you today?"
# text_to_audio_and_play(text)
def text_to_audio_and_play1(text):
    try:
        tts = gTTS(text=text, lang='en')
        filename = "output1.mp3"
        tts.save(filename)
        print(f"Audio file saved as {filename}")

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        os.remove(filename)
        print("Audio playback finished and file deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")