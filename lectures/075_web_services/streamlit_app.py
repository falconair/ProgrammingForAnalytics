import streamlit as st

st.markdown("# Hello")

name = st.text_input("What is your name?")
st.write(f"Hello {name}")

if len(name.strip()) == 0:
    st.warning("You haven't entered your name yet :(")