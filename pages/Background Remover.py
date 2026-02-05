import streamlit as st
import sys
import os
from PIL import Image
import io
from rembg import remove
# --- 1. CONFIG MUST BE FIRST ---
st.set_page_config(page_title="Background Remover", layout="wide")
# --- 2. SETUP PATH & IMPORT UTILS ---
# This ensures we can find utils.py from the pages folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    import utils
    utils.add_bg_and_footer()
except Exception as e:
    # If utils fails, we just ignore it so the app doesn't crash
    pass
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