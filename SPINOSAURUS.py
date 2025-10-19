import streamlit as st

option = st.sidebar.selectbox(
    "Choose the one that you want do see.😄😄😄",
    ("All", "Image", "Video"),
)

st.write("You selected:", option)

st.title("Spinosaurus")
st.write("Spinosaurus are dinosaurs that lived in the Late Cretaceous Period.Here down below is a picture of what a Spinosaurus might have looked like, and a video about Spinosaurus Facts! A Dinosaur Facts video about Spinosaurus, the largest known carnivorous dinosaur. Hope you enjoyed it!!!")

if option == "Image" or option == "All":
    st.subheader("Image")
    st.image("spinosaurus.jpg")

if option == "Video" or option == "All":
    st.subheader("Video")
    st.video("https://www.youtube.com/watch?v=Opilwa5mlpE")

st.write("Hope you all enjoyed it!!!(●'◡'●)")