import streamlit as st

st.set_page_config(page_title='AI MusicVideo Autopilot')
st.title('AI MusicVideo Autopilot')

uploaded_file = st.file_uploader('Upload MP3', type=['mp3'])

if uploaded_file:
    st.success('MP3 uploaded successfully')
    st.info('Pipeline implementation coming in next modules')
