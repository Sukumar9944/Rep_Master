import streamlit as st
import pyttsx3

# Setting Webpage Configurations
st.set_page_config(page_icon="🎶",page_title="Audio Extracter", layout="wide")

st.title('COUNTER APP')

num_range = st.text_input('enter your rep count')

start_button = st.button('Start')
    
if start_button and num_range:
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    for i in range(int(num_range)):
        print(i)
        engine.say(i)
        engine.runAndWait()
        