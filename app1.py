from playsound import playsound
import streamlit as st

st.title('suku')
start = st.button('start')

if start:
    for i in range(10):
        playsound('https://www.freetamilringtones.com/jdownloads/dialogue_ringtones./kamal_haasan/vettaiyadu_villayadu_intro.mp3')
        print('Finished')