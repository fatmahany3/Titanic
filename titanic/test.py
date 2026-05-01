import streamlit as st
st.set_page_config(page_title="Background Image Example", layout="wide")

# Add background image using CSS
page_bg_img = """
<style>
.stApp {
background-image: url("https://media-cldnry.s-nbcnews.com/image/upload/t_social_share_1024x768_scale,f_auto,q_auto:best/rockcms/2023-05/230517-titanic-3d-mb-1259-76694d.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Your app content
st.title("Hello Streamlit!")
st.write("This app has a background image.")