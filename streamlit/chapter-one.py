import streamlit as st
st.title("Hello Chai App")
st.subheader("This is my first Streamlit app")
st.text("Welcome to the world of Streamlit!")  
st.write("Choose your favorite variety of Chai:")
chai = st.selectbox("Select Chai", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai"])
st.write(f"You selected: {chai}")
st.success("Enjoy your Chai!")
