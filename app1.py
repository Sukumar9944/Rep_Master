from playsound import playsound
import os
import streamlit as st

st.title('suku')
start = st.button('start')

abs_path = os.path.abspath('sound.mp3')

if start:
    for i in range(10):
        playsound(abs_path)
        print('Finished')