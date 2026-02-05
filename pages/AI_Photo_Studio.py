import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance
import io
import os
import sys
import requests
from streamlit_drawable_canvas import st_canvas
# --- PATH SETUP & UTILS ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Apply Glass Theme
try:
    utils.add_bg_and_footer()
except:
    pass
st.title("✨ AI Photo Studio")
st.markdown("Use Deep Learning to **upscale quality** or **remove watermarks**.")
# --- HELPER: DOWNLOAD AI MODEL (EDSR) ---
# We download the model file once so the app can run it.
MODEL_PATH = "EDSR_x2.pb"
MODEL_URL = "https://github.com/Saafke/EDSR_Tensorflow/raw/master/models/EDSR_x2.pb"
def load_model():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("📥 Downloading AI Model (First time run)..."):
            try:
                r = requests.get(MODEL_URL, allow_redirects=True)
                with open(MODEL_PATH, 'wb') as f:
                    f.write(r.content)
            except:
                st.error("Could not download model. Check internet connection.")
    return MODEL_PATH
# --- TABS FOR TOOLS ---
tab1, tab2 = st.tabs(["💧 Watermark Remover", "🚀 Quality Enhancer"])
# ==========================================
# TAB 1: WATERMARK REMOVER (INPAINTING)
# ==========================================
with tab1:
    st.subheader("1. Remove Unwanted Objects/Text")
    st.info("👇 **Instructions:** Draw over the watermark with the brush, then click 'Clean Image'.")
    # Upload
    uploaded_file_rem = st.file_uploader("Upload Image to Clean", type=["jpg", "png", "jpeg"], key="rem")
    if uploaded_file_rem:
        # Convert to RGB for canvas
        image_pil = Image.open(uploaded_file_rem).convert("RGB")
        # Resize for display if too large (prevents lag)
        max_width = 700
        if image_pil.width > max_width:
            ratio = max_width / image_pil.width
            new_height = int(image_pil.height * ratio)
            image_pil = image_pil.resize((max_width, new_height))
        # --- DRAWING CANVAS ---
        # stroke_width = brush size
        stroke_width = st.slider("Brush Size", 1, 50, 15)
        canvas_result = st_canvas(
            fill_color="rgba(255, 0, 0, 0.3)",  # Red transparent mask
            stroke_width=stroke_width,
            stroke_color="#ff0000",
            background_image=image_pil,
            update_streamlit=True,
            height=image_pil.height,
            width=image_pil.width,
            drawing_mode="freedraw",
            key="canvas",
        )
        # PROCESS BUTTON
        if st.button("✨ Clean Image"):
            if canvas_result.image_data is not None:
                # 1. Prepare Image & Mask
                img_array = np.array(image_pil)
                # The canvas returns RGBA, we need just the Alpha channel for the mask
                mask_data = canvas_result.image_data[:, :, 3] 
                # 2. Run Inpainting (Telea Algorithm)
                # This looks at pixels around the mask and fills it in
                restored_img = cv2.inpaint(img_array, mask_data.astype(np.uint8), 3, cv2.INPAINT_TELEA)
                # 3. Show Result
                st.success("Object removed!")
                st.image(restored_img, caption="Cleaned Image", use_container_width=True)
                # 4. Download
                restored_pil = Image.fromarray(restored_img)
                buf = io.BytesIO()
                restored_pil.save(buf, format="PNG")
                st.download_button("📥 Download Result", buf.getvalue(), "cleaned.png", "image/png")
# ==========================================
# TAB 2: QUALITY ENHANCER (SUPER RES)
# ==========================================
with tab2:
    st.subheader("2. Deep Learning Upscaler (EDSR)")
    st.write("This uses a **Deep Neural Network** to increase resolution without losing clarity.")
    uploaded_file_enh = st.file_uploader("Upload Low-Res Image", type=["jpg", "png", "jpeg"], key="enh")
    if uploaded_file_enh:
        image_enh = Image.open(uploaded_file_enh).convert("RGB")
        st.image(image_enh, caption="Original", width=300)
        if st.button("🚀 Enhance Quality (2x Zoom)"):
            with st.spinner("🤖 AI is dreaming up new pixels..."):
                try:
                    # 1. Load the Model
                    model_path = load_model()
                    sr = cv2.dnn_superres.DnnSuperResImpl_create()
                    sr.readModel(model_path)
                    # Set the model to upscale by 2x
                    sr.setModel("edsr", 2) 
                    # 2. Process
                    # Convert PIL to OpenCV format (RGB -> BGR)
                    img_cv = cv2.cvtColor(np.array(image_enh), cv2.COLOR_RGB2BGR)
                    # Upscale
                    upscaled_cv = sr.upsample(img_cv)
                    # Convert back to PIL (BGR -> RGB)
                    upscaled_rgb = cv2.cvtColor(upscaled_cv, cv2.COLOR_BGR2RGB)
                    final_image = Image.fromarray(upscaled_rgb)
                    # 3. Sharpen slightly for crispness
                    enhancer = ImageEnhance.Sharpness(final_image)
                    final_image = enhancer.enhance(1.1)
                    st.success("✅ Enhancement Complete! Resolution doubled.")
                    # Show comparison
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.write("**Original**")
                        st.image(image_enh, use_container_width=True)
                    with col_b:
                        st.write("**Enhanced AI**")
                        st.image(final_image, use_container_width=True)
                    # Download
                    buf2 = io.BytesIO()
                    final_image.save(buf2, format="PNG")
                    st.download_button("📥 Download HD Image", buf2.getvalue(), "enhanced.png", "image/png")
                except Exception as e:
                    st.error(f"Error: {e}. (Make sure opencv-contrib-python is not conflicting)")