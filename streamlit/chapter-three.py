import streamlit as st
st.title("Chai Taste Poll")
col1, col2 = st.columns(2)
with col1:
    st.header("Masala Chai")
    st.image("https://www.thespicehouse.com/cdn/shop/articles/Chai_Masala_Tea_1200x1200.jpg?v=1606936195", width=150)
    vote1 = st.button("Vote for Masala Chai")
with col2:  
    st.header("Adrak Chai")
    st.image("https://budleaf.com/wp-content/uploads/2023/08/Adrak-masala-chai-scaled.jpeg", width=150)

    vote2 = st.button("Vote for Adrak Chai")
if vote1:
    st.success("You voted for Masala Chai!")
elif vote2:
    st.success("You voted for Adrak Chai!")
name = st.sidebar.text_input("Enter your name to submit your vote")
tea = st.sidebar.selectbox("Select your favorite Chai", ["Masala Chai", "Adrak Chai"])

st.write(f"Voter Name: {name}")
st.write(f"Favorite Chai: {tea}")   

with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water and milk in a pot.
    2. Add tea leaves and let it simmer.    
             """)
st.markdown("### Thank you for participating in the Chai Taste Poll!")
st.markdown("> Blockquote")