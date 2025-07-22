import streamlit as st

# App title and description
st.title("My Awesome Streamlit Project")
st.write("Hello, world! This is a basic app deployed on Streamlit Cloud. Customize me further!")

# Add some interactive elements (example: a slider and button)
number = st.slider("Pick a number", 0, 100, 50)
if st.button("Show Result"):
    st.success(f"You picked {number}! Great choice.")