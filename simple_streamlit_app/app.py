import streamlit as st
from PIL import Image

st.title('Страничка Алтышевой Марии')


img = Image.open("me.jpg")
st.image(img, width=500)
