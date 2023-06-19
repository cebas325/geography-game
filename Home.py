# Home page of the application
import streamlit as st

from database.db_manager import create_spain_table

# Creating all the tables
create_spain_table()

st.markdown("# Welcome to Europe's Goegraphy game!")
st.markdown("""Test your geographical skills by different levels of detail, switch to the country-mode you wanna play
and compare your results with those from other people.
To get started, fill out the welcoming form with you personal data and choose a country and level of 
detail.""")
name = st.text_input("Enter your name: ")
st.markdown(f"Hi, {name}!")