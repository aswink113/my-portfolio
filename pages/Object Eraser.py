import streamlit as st
import sys
import os

# This block is needed so the pages folder can find utils.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils 

# Apply the style
utils.add_bg_and_footer()

# ... The rest of your existing code ...import streamlit as st

st.title("🔮 Future Tools")
st.write("These advanced AI tools are currently under development!")

# List of future features
tools = {
    "Object Eraser": "Removes unwanted people or objects from photos using Inpainting AI.",
    "Video Compressor": "Compresses video files using FFMPEG (Coming soon).",
    "Old Photo Restoration": "Fixes scratches on old images."
}

for tool, desc in tools.items():
    with st.expander(f"🚧 {tool}"):
        st.write(desc)
        st.warning("Status: Coding in progress...")

# A dummy email subscription box
st.divider()
st.subheader("Get notified when these are ready")
email = st.text_input("Enter your email")
if st.button("Subscribe"):
    if email:
        st.success("You are on the list!")