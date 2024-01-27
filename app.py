import streamlit as st
import pyttsx3

# Setting Webpage Configurations
st.set_page_config(page_icon="",page_title="Audio Extracter", layout="wide")

st.header(':red[Rep Master] ®')
st.caption('Feel the rhythm, own the beat !')

num_range = st.text_input('Enter your Rep Count')

speed = st.text_input('Enter the Speed')

start_button = st.button('Start')

def master(speed, num_range):    
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    for i in range(1, int(num_range)+1):
        engine.say(i)
        engine.runAndWait()


if start_button and num_range and speed:
    master(int(speed), num_range)
    st.success('RepMaster - Program Completed 🏋️‍')

