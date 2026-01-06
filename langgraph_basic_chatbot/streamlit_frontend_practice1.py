import streamlit as st

with st.chat_message("user"):
    st.text("Hi")

with st.chat_message("assistant"):
    st.text("Hello! How can I assist you today?")

with st.chat_message("user"):
    st.text("My name is Wardah")

user_input = st.chat_input("Type your message here...")
if user_input:
    with st.chat_message("user"):
        st.text(user_input)

# is file me sabse pehle user ke aur assistant ke messages ko hard code kia hai phr chat input banaya hai jisse user apna message
#  de sakta hai, user message showhoga uske baad agr user dosra message lkh kar enter karega tou purana message override hojaiga