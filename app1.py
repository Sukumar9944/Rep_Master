import streamlit as st

def main():
    st.title("Audio Player App")

    audio_url = st.text_input("Enter the URL of the audio file:")
    play_button = st.button("Start Playing")

    if play_button:
        if audio_url:
            st.text("Playing audio...")
            # Use JavaScript to play audio in the browser
            st.markdown(f'<audio src="{audio_url}" controls autoplay></audio>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a valid audio URL.")

if __name__ == "__main__":
    main()
