import streamlit as st
st.title("Chai Maker App")
if st.button("Make Chai"):
    st.success("Your Chai is being prepared!")
add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala added to your Chai.")

tea_type = st.radio("Pick your chai base", ["Milk", "Water", "Almond Milk"])
st.write(f"You selected: {tea_type} as your chai base.")

flavour = st.selectbox("Choose a flavour", ["Cardamom", "Ginger", "Saffron", "Tulsi"])
st.write(f"You selected: {flavour} flavour.")

sugar_level = st.slider("Select sugar level (in tsp)", 0, 5, 2) # 0-5 slider range and 2 is the default value
st.write(f"Sugar level set to: {sugar_level} tsp")

cups = st.number_input("Enter the number of cups you want", min_value=1, max_value=10, step=1)
st.write(f"You want to make {cups} cup(s) of Chai.")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Your Chai will be ready soon.")
dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth is: {dob}")