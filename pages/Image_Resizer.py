import streamlit as st
from PIL import Image
import io
# 1. Page Config
st.set_page_config(page_title="Image Resizer", layout="wide")
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

