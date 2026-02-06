import streamlit as st
import base64
import os
import streamlit.components.v1 as components

# --------------------------------------------------
# 1. PAGE CONFIG (NO SIDEBAR)
# --------------------------------------------------
st.set_page_config(
    page_title="ASWIN K | AI Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# 2. GLOBAL CSS (GLASS + NO SIDEBAR)
# --------------------------------------------------
st.markdown("""
<style>
/* APP BACKGROUND */
.stApp {
    background: radial-gradient(circle at 10% 20%, rgb(10,20,40) 0%, rgb(5,10,20) 90%);
    background-attachment: fixed;
    color: white;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}

/* REMOVE STREAMLIT UI */
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stSidebar"],
footer,
div[class^="viewerBadge"] {
    display: none !important;
}

/* HEADER TEXT */
.header-text {
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(90deg, #00C9FF, #92FE9D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}

/* HERO */
.hero-container {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 8rem 2rem;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}

.hero-title {
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(to right, #ffffff, #a0a0a0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-buttons {
    display: flex;
    gap: 20px;
}

/* TOOL BUTTONS */
div.stButton > button {
    background: rgba(255,255,255,0.04) !important;
    border-radius: 20px !important;
    height: 160px;
}

/* ABOUT */
.about-box {
    background: rgba(255,255,255,0.03);
    border-radius: 24px;
    padding: 40px;
    border-left: 4px solid #00ADB5;
}

/* MOBILE */
@media (max-width: 600px) {
    .hero-container { padding: 3rem 1.5rem; }
    .hero-title { font-size: 2.4rem; }
    .hero-buttons { flex-direction: column; }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. HEADER (HOME LEFT • NAME CENTER • CONTACT RIGHT)
# --------------------------------------------------
c1, c2, c3 = st.columns([1, 2, 1])

with c1:
    st.markdown("🏠 **Home**")

with c2:
    st.markdown('<div class="header-text">ASWIN K</div>', unsafe_allow_html=True)

with c3:
    st.link_button("📧 Contact Me", "mailto:contact@aswin.ai", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# 4. HERO SECTION
# --------------------------------------------------
def get_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_style = "background: linear-gradient(120deg, #1c1e26, #2a2d3a);"

if os.path.exists("profile.jpg"):
    img_b64 = get_img_as_base64("profile.jpg")
    bg_style = f"""
        background:
        linear-gradient(to right, rgba(10,20,40,0.95), rgba(10,20,40,0.6)),
        url("data:image/jpg;base64,{img_b64}");
        background-size: cover;
        background-position: center;
    """

st.markdown(f"""
<div class="hero-container" style="{bg_style}">
    <div style="max-width:750px">
        <h3 style="color:#00C9FF; letter-spacing:3px;">HELLO, I AM A</h3>
        <h1 class="hero-title">Data Scientist</h1>
        <p style="font-size:1.3rem; color:#E0E0E0;">
            I build <b>intelligent systems</b> using
            <span style="color:#00C9FF">Generative AI</span> &
            <span style="color:#92FE9D">Deep Learning</span>
        </p>
        <div class="hero-buttons">
            <a href="https://github.com/aswin" target="_blank"
               style="background:linear-gradient(90deg,#00C9FF,#92FE9D);
               padding:14px 35px;border-radius:30px;color:black;font-weight:bold;">
               View Projects
            </a>
            <a href="https://linkedin.com/in/aswin" target="_blank"
               style="background:#0077b5;padding:14px 35px;
               border-radius:30px;color:white;font-weight:bold;">
               LinkedIn
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 5. ABOUT
# --------------------------------------------------
st.subheader("👨‍💻 About Me")
st.markdown("""
<div class="about-box">
    <p style="font-size:1.15rem; line-height:1.8;">
        Data Scientist and AI Python Trainer with a Diploma in Electronics.
        Specialized in ML, Computer Vision and Generative AI.
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 6. TOOLS GRID
# --------------------------------------------------
st.subheader("🚀 Try My AI Tools")

tools = [
    ("📷 Background Remover", "pages/Background_Remover.py"),
    ("✨ AI Photo Studio", "pages/AI_Photo_Studio.py"),
    ("📄 PDF Splitter", "pages/PDF_Splitter.py"),
    ("🧼 Object Eraser", "pages/Object_Eraser.py"),
    ("🎬 Movie Link Finder", "pages/Movie_Link_Finder.py"),
    ("📉 Image Compressor", "pages/Image_Compressor.py"),
]

cols = st.columns(3)
for i, (label, file) in enumerate(tools):
    with cols[i % 3]:
        if st.button(label, key=file, use_container_width=True):
            st.switch_page(file)
