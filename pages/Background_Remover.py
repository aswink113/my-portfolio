import streamlit as st
from PIL import Image
import io
from rembg import remove
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
# ... REST OF YOUR TOOL CODE BELOW ...
# --- 2. SETUP PATH & IMPORT UTILS ---
# --- 3. MAIN APP CONTENT ---
st.title("📷 Background Remover")
st.markdown("### Upload an image, and AI will magically remove the background.")
# --- LAYOUT: Two Columns ---
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.info("👇 **Step 1: Upload Image**")
    uploaded_file = st.file_uploader("Choose a JPG or PNG", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        # Save uploaded file to a variable
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_container_width=True)
with col2:
    if uploaded_file:
        st.info("👇 **Step 2: Magic Time!**")
        # The Magic Button
        if st.button("✨ Remove Background Now", type="primary"):
            with st.spinner("🤖 AI is processing... please wait..."):
                try:
                    # 1. Convert image to bytes
                    buf = io.BytesIO()
                    image.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    # 2. RUN REMBG (The AI)
                    output_image = remove(byte_im)
                    # 3. Create PIL Image from result
                    val = io.BytesIO(output_image)
                    img_out = Image.open(val)
                    # 4. Show Result
                    st.success("✅ Done!")
                    st.image(img_out, caption="Background Removed", use_container_width=True)
                    # 5. Download Button
                    st.download_button(
                        label="📥 Download Transparent Image",
                        data=val.getvalue(),
                        file_name="no_bg_image.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
    else:
        st.write("Results will appear here...")


