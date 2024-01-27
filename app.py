import streamlit as st
import pyttsx3

# Setting Webpage Configurations
st.set_page_config(page_icon="🎶",page_title="Audio Extracter", layout="wide")

st.title('COUNTER APP')

engine = pyttsx3.init()
engine.setProperty('rate', 100)

num_range = st.text_input('enter your rep count')

start_button = st.button('Start')
    
if start_button and num_range:
    for i in range(int(num_range)):
        print(i)
        engine.say(i)
        engine.runAndWait()
        