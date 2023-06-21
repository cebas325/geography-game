# Home page of the application
import streamlit as st

from database.db_manager import create_spain_table

# Creating all the tables
create_spain_table()

st.markdown("# Welcome to Europe's Geography game! :earth_africa:")
st.markdown("""Test your geographical skills by different levels of detail, switch to the country-mode you wanna play
and compare your results with those from other people.

To get started, please fill out the welcoming form below.""")

name = st.text_input("Enter your name and/or surname")
    
country = st.selectbox(
    'Select a starting country',
    ['Spain', 'Austria', 'Germany'],
    index=0
)

level = st.selectbox(
    'Select a starting level of difficulty',
    ['Easy', 'Medium', 'Hard'],
    index=0
)

st.info("""Both country and level of difficulty can be changed at any moment in the `Settings` page""")
st.write("")

if name:
    st.markdown(f"Hi, :blue[{name}], very welcome! :blush:")
st.markdown(":point_left: Please, use the sidebar in the left to navigate through the app!")