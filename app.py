import streamlit as st
from PIL import Image

# Title
st.title("🌸 My Hosted Pookalam")

st.write("This is my Python Turtle Pookalam project with Kathakali GIF!")

# Show the Kathakali GIF
st.image("kathakali.gif")

# Show the source code of demo.py
with open("demo.py", "r") as f:
    st.code(f.read(), language="python")