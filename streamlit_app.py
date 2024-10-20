from streamlit_option_menu import option_menu
import streamlit as st

selected = option_menu("Main Menu", ["Home", "Settings"], 
    icons=['house', 'gear'], menu_icon="cast", default_index=0)

st.write(f"Selected option: {selected}")
