import streamlit as st


st.set_page_config(layout="wide", page_title="Face Verification App")

st.write("## Verificate your employee's face")
st.write("### DSM 5014 Derin Öğrenme Yöntemleri ve Uygulamaları")

st.write(
    ":dog: Try implementing face verification using one-shot learning and test the model's ability to learn from a single instance. This code is open source and available [here](https://github.com/tyler-simons/BackgroundRemoval) and create by Alaaeddin:grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
