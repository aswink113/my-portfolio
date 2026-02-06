import streamlit as st
import base64
import os
# --------------------------------------------------
# 1. PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="ASWIN K | AI Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --------------------------------------------------
# 2. GLOBAL CSS
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
/* HEADER */
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
    border-radius: 26px;
    padding: 8rem 3rem;
    margin-bottom: 3rem;
    box-shadow: 0 25px 60px rgba(0,0,0,0.6);
    position: relative;
    overflow: hidden;
}
/* DARK OVERLAY */
.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to right,
        rgba(5,10,25,0.95),
        rgba(5,10,25,0.6),
        rgba(5,10,25,0.3)
    );
}
/* HERO CONTENT */
.hero-content {
    position: relative;
    max-width: 780px;
    z-index: 2;
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
    margin-top: 25px;
}
/* MOBILE */
@media (max-width: 768px) {
    .hero-container {
        padding: 4rem 2rem;
    }
    .hero-title {
        font-size: 2.6rem;
    }
    .hero-buttons {
        flex-direction: column;
    }
}
</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# 3. HEADER
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
# 4. HERO BACKGROUND IMAGE (BASE64 SAFE)
# --------------------------------------------------
def image_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()
hero_bg = "background: linear-gradient(120deg, #1c1e26, #2a2d3a);"
if os.path.exists("profile.jpg"):
    img_b64 = image_to_base64("profile.jpg")
    hero_bg = f"""
        background-image:
        linear-gradient(
            to right,
            rgba(5,10,25,0.95),
            rgba(5,10,25,0.65),
            rgba(5,10,25,0.3)
        ),
        url("data:image/jpeg;base64,{img_b64}");
        background-size: cover;
        background-position: center;
    """
# --------------------------------------------------
# 5. HERO SECTION
# --------------------------------------------------
st.markdown(f"""
<div class="hero-container" style="{hero_bg}">
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <h3 style="color:#00C9FF; letter-spacing:3px;">HELLO, I AM A</h3>
        <h1 class="hero-title">Data Scientist</h1>
        <p style="font-size:1.3rem; color:#E0E0E0; max-width:650px;">
            I build <b>intelligent systems</b> using
            <span style="color:#00C9FF">Generative AI</span> &
            <span style="color:#92FE9D">Deep Learning</span>
        </p>
        <div class="hero-buttons">
            <a href="https://github.com/aswin" target="_blank"
               style="background:linear-gradient(90deg,#00C9FF,#92FE9D);
               padding:14px 36px;border-radius:30px;
               color:black;font-weight:700;text-decoration:none;">
               View Projects
            </a>
            <a href="https://linkedin.com/in/aswin" target="_blank"
               style="background:#0077b5;padding:14px 36px;
               border-radius:30px;color:white;
               font-weight:700;text-decoration:none;">
               LinkedIn
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
# --------------------------------------------------
# 6. ABOUT
# --------------------------------------------------
st.subheader("👨‍💻 About Me")
st.markdown("""
<div style="
    background: rgba(255,255,255,0.03);
    border-radius: 24px;
    padding: 40px;
    border-left: 4px solid #00ADB5;
">
    <p style="font-size:1.15rem; line-height:1.8;">
        Data Scientist and AI Python Trainer with a Diploma in Electronics.
        Specialized in Machine Learning, Computer Vision and Generative AI.
    </p>
</div>
""", unsafe_allow_html=True)
# --------------------------------------------------
# 7. FOOTER SPACE
# --------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
