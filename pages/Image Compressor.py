import streamlit as st
import sys
import os

# This block is needed so the pages folder can find utils.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils 

# Apply the style
utils.add_bg_and_footer()

# ... The rest of your existing code ...import streamlit as st
from PIL import Image
import io

st.title("Image Compressor")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])
quality_val = st.slider("Quality (10=Low, 95=High)", 10, 95, 60)

if uploaded_file:
    img = Image.open(uploaded_file)
    st.write(f"Original Size: {uploaded_file.size / 1024:.2f} KB")
    
    if st.button("Compress"):
        buf = io.BytesIO()
        if img.mode in ("RGBA", "P"): img = img.convert("RGB") # JPG doesn't support transparency
        
        img.save(buf, format="JPEG", quality=quality_val, optimize=True)
        byte_im = buf.getvalue()
        
        st.write(f"Compressed Size: {len(byte_im) / 1024:.2f} KB")
        st.download_button("Download Compressed", byte_im, "compressed.jpg", "image/jpeg")