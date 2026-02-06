import streamlit as st
from PIL import Image
import io
# 1. Page Config
st.set_page_config(page_title="Image Resizer", layout="wide")
# --- MAIN APP LOGIC ---
st.title("🖼️ Smart Image Resizer")
st.markdown("Resize your images to exact pixel dimensions while maintaining quality.")
# Upload Section
uploaded_file = st.file_uploader("Upload an Image (JPG/PNG)", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    original_width, original_height = image.size
    # Show current info in a glass box
    st.info(f"📏 Original Size: **{original_width} x {original_height} pixels**")
    # Display Image (Thumbnail)
    st.image(image, caption="Original Image", use_container_width=True)
    st.write("---")
    st.subheader("⚙️ Resize Settings")
    # Layout for inputs
    col1, col2, col3 = st.columns(3)
    with col1:
        # Width Input
        new_width = st.number_input("New Width (px)", value=original_width, min_value=1)
    with col2:
        # Height Input
        new_height = st.number_input("New Height (px)", value=original_height, min_value=1)
    with col3:
        # Aspect Ratio Helper
        st.write("") # Spacer
        st.write("") # Spacer
        if st.checkbox("🔒 Maintain Aspect Ratio", value=True):
            # If checked, we recalculate height based on width change
            aspect_ratio = original_height / original_width
            # Note: In Streamlit, real-time sync is tricky, so we calculate strictly on the button press below
            # or we guide the user.
            st.caption(f"Suggested Height for {new_width}px width: **{int(new_width * aspect_ratio)}px**")
    # --- RESIZE BUTTON ---
    if st.button("🚀 Resize Image Now"):
        # 1. Resize Logic
        resized_image = image.resize((new_width, new_height))
        # 2. Show Result
        st.success(f"✅ Resized to {new_width}x{new_height} pixels!")
        st.image(resized_image, caption=f"Resized Image ({new_width}x{new_height})", use_container_width=True)
        # 3. Prepare Download
        buf = io.BytesIO()
        # Save as the original format
        img_format = image.format if image.format else "PNG"
        resized_image.save(buf, format=img_format)
        byte_im = buf.getvalue()
        # 4. Download Button
        st.download_button(
            label="📥 Download Resized Image",
            data=byte_im,
            file_name=f"resized_{uploaded_file.name}",
            mime=f"image/{img_format.lower()}"
        )

