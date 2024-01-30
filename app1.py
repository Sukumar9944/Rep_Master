from gtts import gTTS
import os
import pygame
import streamlit as st

st.title('sample')

start = st.button('starting')

if start:
    for i in range(1, 10):
        tts = gTTS(text=f"{i}", lang="en", slow=False, timeout=10)
        tts.save("sound.mp3")

        abs_path = os.path.abspath(f"sound.mp3")

        pygame.init()

        # Load the audio file
        audio = pygame.mixer.music.load(abs_path)

        pygame.mixer.music.play()

        # Allow time for the sound to play
        pygame.time.delay(1700)  # Adjust the delay as needed

        # Quit pygame
        pygame.quit()

        os.remove(abs_path)