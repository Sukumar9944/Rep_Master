import streamlit as st

# Setting Webpage Configurations
st.set_page_config(page_icon="©",page_title="Rep Master", layout="wide")

def main():
    st.header(':red[Rep Master] ®')
    st.caption('Feel the rhythm, own the beat !')

    num_range = st.text_input('Enter your Rep Count')

    start_button = st.button('Start')

    if num_range == '5':
        audio_url = 'https://www.freetamilringtones.com/jdownloads/dialogue_ringtones./kamal_haasan/vettaiyadu_villayadu_intro.mp3'
    

    if start_button and audio_url and num_range:
        st.text("RepMaster - Program Started 🏋️")
        # Use JavaScript to play audio in the browser
        st.markdown(f'<audio src="{audio_url}" controls autoplay></audio>', unsafe_allow_html=True)
        st.success('RepMaster - Program Completed 🏋️‍')
    else:
        st.warning("Please check your Internet Connection.")

if __name__ == "__main__":
    main()
