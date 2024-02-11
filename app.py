import streamlit as st

# Setting Webpage Configurations
st.set_page_config(page_icon="©",page_title="Rep Master", layout="wide")

@st.cache_resource
def main():
    st.header(':red[Rep Master] ®')
    st.caption('Feel the rhythm, own the beat !')

    num_range = st.selectbox('Select your Rep Count', ['5', '10', '15', '20'])

    if num_range == '5':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoFive.mp3'
    
    elif num_range == '10':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoTen.mp3'

    elif num_range == '15':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoFifteen.mp3'

    elif num_range == '20':
        audio_url = 'https://raw.githubusercontent.com/Sukumar9944/Rep_Master/main/Sounds/OnetoTwenty.mp3'

    return audio_url
        
run_app = main()

start_button = st.button('Start')

if run_app and start_button:
    st.success("RepMaster - Program Started 🏋️")
    # Use JavaScript to play audio in the browser
    st.markdown(f'<audio src="{run_app}" controls autoplay></audio>', unsafe_allow_html=True)
