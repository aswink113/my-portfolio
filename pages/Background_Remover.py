import streamlit as st
from PIL import Image
import io
from rembg import remove
# --------------------------------------------------
# PAGE CONFIG (NO SIDEBAR)
# --------------------------------------------------
st.set_page_config(
    page_title="Background Remover | ASWIN K",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --------------------------------------------------
# CACHE REMBG (CRITICAL FIX)
# --------------------------------------------------
@st.cache_resource
def load_rembg():
    return remove
# --------------------------------------------------
# GLOBAL CSS + JS (KILL SIDEBAR PERMANENTLY)
# --------------------------------------------------
st.markdown("""
<style>
/* KILL SIDEBAR */
section[data-testid="stSidebar"] { display: none !important; }
div[data-testid="collapsedControl"] { display: none !important; }
div[data-testid="stSidebarNav"] { display: none !important; }
/* REMOVE STREAMLIT HEADER & FOOTER */
header[data-testid="stHeader"] { display: none !important; }
footer { display: none !important; }
/* FULL WIDTH */
.block-container {
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}
/* APP BACKGROUND */
.stApp {
    background: radial-gradient(circle at 10% 20%, rgb(10,20,40), rgb(5,10,20));
    color: white;
}
/* CUSTOM HEADER */
.header-text {
    font-size: 24px;
    font-weight: 800;
    background: linear-gradient(90deg, #00C9FF, #92FE9D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}
</style>

<script>
/* FORCE REMOVE SIDEBAR AFTER RERUN */
const sidebar = parent.document.querySelector('section[data-testid="stSidebar"]');
if (sidebar) sidebar.remove();
</script>
""", unsafe_allow_html=True)
# --------------------------------------------------
# CUSTOM HEADER BAR
# --------------------------------------------------
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    st.page_link("../Home.py", label="🏠 Home", use_container_width=True)
with c2:
    st.markdown('<div class="header-text">ASWIN K</div>', unsafe_allow_html=True)
with c3:
    st.link_button("📧 Contact", "mailto:contact@aswin.ai", use_container_width=True)
st.markdown("<hr>", unsafe_allow_html=True)
# --------------------------------------------------
# MAIN APP CONTENT
# --------------------------------------------------
st.title("📷 Background Remover")
st.markdown("### Upload an image and AI will remove the background ✨")
col1, col2 = st.columns(2, gap="large")
# ---------------- LEFT COLUMN ----------------
with col1:
    st.info("👇 **Step 1: Upload Image**")
    uploaded_file = st.file_uploader(
        "Choose a JPG or PNG",
        type=["jpg", "jpeg", "png"]
    )
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_container_width=True)
# ---------------- RIGHT COLUMN ----------------
with col2:
    if uploaded_file:
        st.info("👇 **Step 2: Magic Time!**")
        run = st.button("✨ Remove Background Now", type="primary")
        if run:
            with st.spinner("🤖 AI is processing..."):
                try:
                    # Load cached rembg
                    rembg = load_rembg()
                    # Convert image to bytes
                    buf = io.BytesIO()
                    image.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    # Remove background
                    output = rembg(byte_im)
                    # Convert output to image
                    result_buf = io.BytesIO(output)
                    img_out = Image.open(result_buf)
                    st.success("✅ Done!")
                    st.image(
                        img_out,
                        caption="Background Removed",
                        use_container_width=True
                    )
                    st.download_button(
                        label="📥 Download Transparent Image",
                        data=result_buf.getvalue(),
                        file_name="no_bg_image.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
    else:
        st.write("Results will appear here...")
