import streamlit as st
from PIL import Image
import io
# 1. Page Config
st.set_page_config(page_title="Image Resizer", layout="wide")
# 2. Back to Home Button
if st.button("← Back to Home"):
    st.switch_page("Home.py")
# 3. Main App Logic
st.title("🖼️ Smart Image Resizer")
st.write("Upload an image to resize it.")
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"Original Size: {image.size}", use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        new_width = st.number_input("Width", min_value=1, value=image.width)
    with col2:
        new_height = st.number_input("Height", min_value=1, value=image.height)
    if st.button("Resize Now"):
        resized_image = image.resize((new_width, new_height))
        st.image(resized_image, caption=f"New Size: {resized_image.size}", use_container_width=True)
        # Prepare Download
        buf = io.BytesIO()
        resized_image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button("Download Resized Image", data=byte_im, file_name="resized.png", mime="image/png")
