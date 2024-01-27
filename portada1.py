import streamlit as st
import base64

st.set_page_config(page_title='RIMESOFT', page_icon='☄️', initial_sidebar_state='collapsed')

@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#path_background_img = r'./img/portada.png'

img = get_base64_of_bin_file(r'./img/portada.png')

page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64, {img}");
    background-size: cover;
    }
    </style>
    '''
st.markdown(page_bg_img,unsafe_allow_html=True)