import streamlit as st
from Home import country
from utils.display import get_flag

st.set_page_config(
    page_icon=":boom:",
    initial_sidebar_state="collapsed"
)

flag = get_flag(country)
st.markdown("#### Ready to start? :smirk:")
st.markdown(f"Currently playing in **{country}** {flag} mode ")