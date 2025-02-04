import streamlit as st

st.title("My V-Day Website 💖")
st.write("Welcome to my Valentine's Day themed website!")

# Example interactive elements
name = st.text_input("Enter your name:")
if name:
    st.write(f"Happy Valentine's Day, {name}! ❤️")
