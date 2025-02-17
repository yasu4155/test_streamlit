import streamlit as st

tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

tab1.button("tab1 button")

tab2.text_input("tab2 text_input")

tab3.checkbox("tab3 checkbox")