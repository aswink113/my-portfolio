import streamlit as st
import sys
import os
# ... The rest of your existing code ...import streamlit as st
from PIL import Image
import io
# --- HEADER CONFIGURATION (PASTE THIS ON EVERY PAGE) ---
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    /* HIDE SIDEBAR & DEFAULT HEADER */
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    [data-testid="stHeader"] {display: none;}
    /* CUSTOM HEADER STYLE */
    .header-text {
        font-family: sans-serif;
        font-size: 24px;
        font-weight: 800;
        background: linear-gradient(90deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 10px;
    }
    .stApp { background: radial-gradient(circle at 10% 20%, rgb(10, 20, 40) 0%, rgb(5, 10, 20) 90%); color: white; }
    </style>
""", unsafe_allow_html=True)
# HEADER LAYOUT
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    st.page_link("Home.py", label="🏠 Home", use_container_width=True)
with c2:
    st.markdown('<div class="header-text">ASWIN K</div>', unsafe_allow_html=True)
with c3:
    st.link_button("📧 Contact", "mailto:contact@aswin.ai", use_container_width=True)
st.write("---")
# --- END HEADER ---
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

