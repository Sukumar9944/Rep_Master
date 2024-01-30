import streamlit as st

# Setting Webpage Configurations
st.set_page_config(page_icon="©",page_title="Rep Master", layout="wide")

def main():
    st.header(':red[Rep Master] ®')
    st.caption('Feel the rhythm, own the beat !')

    num_range = st.selectbox('Select your Rep Count', ['5', '10', '15', '20'])

    start_button = st.button('Start')

    if num_range == '5':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoFive.mp3'
    
    elif num_range == '10':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoTen.mp3'

    elif num_range == '15':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoFifteen.mp3'

    elif num_range == '20':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoTwenty.mp3'
        

    if start_button and audio_url and num_range:
        st.success("RepMaster - Program Started 🏋️")
        # Use JavaScript to play audio in the browser
        st.markdown(f'<audio src="{audio_url}" controls autoplay></audio>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()