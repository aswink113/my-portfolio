import streamlit as st
import base64
import os
import streamlit.components.v1 as components
# --------------------------------------------------
# 1. PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="ASWIN K | AI Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --------------------------------------------------
# 2. GLOBAL CSS + SCROLL ANIMATIONS
# --------------------------------------------------
st.markdown("""
<style>
/* GLOBAL */
.stApp {
    background: radial-gradient(circle at 10% 20%, rgb(10,20,40) 0%, rgb(5,10,20) 90%);
    background-attachment: fixed;
    color: white;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}
/* CLEAN UI */
[data-testid="stHeader"],
[data-testid="stToolbar"],
footer,
div[class^="viewerBadge"] {
    display: none;
}
/* HEADER */
.header-text {
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(90deg, #00C9FF, #92FE9D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-top: 20px;
}
/* HERO */
.hero-container {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 8rem 2rem;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}
/* TITLES */
.hero-title {
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(to right, #fff, #aaa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-buttons {
    display: flex;
    gap: 20px;
}
/* ABOUT */
.about-box {
    background: rgba(255,255,255,0.03);
    border-radius: 24px;
    padding: 40px;
    border-left: 4px solid #00ADB5;
}
/* BUTTON CARDS */
div.stButton > button {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 20px !important;
    height: 160px;
}
/* MOBILE */
@media (max-width: 600px) {
    .hero-container { padding: 3rem 1.5rem; }
    .hero-title { font-size: 2.4rem; }
    .hero-buttons { flex-direction: column; }
}
/* ---------------- SCROLL ANIMATIONS ---------------- */
.reveal {
    opacity: 0;
    transform: translateY(40px);
    transition: all 0.9s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.reveal.active {
    opacity: 1;
    transform: translateY(0);
}
.reveal-left { transform: translateX(-60px); }
.reveal-right { transform: translateX(60px); }
.reveal-scale { transform: scale(0.92); }
.reveal-left.active,
.reveal-right.active,
.reveal-scale.active {
    opacity: 1;
    transform: none;
}
</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# 3. HEADER
# --------------------------------------------------
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    st.page_link("pages/Home.py", label="🏠 Home", use_container_width=True)
with c2:
    st.markdown('<div class="header-text">ASWIN K</div>', unsafe_allow_html=True)
with c3:
    st.link_button("📧 Contact Me", "mailto:contact@aswin.ai", use_container_width=True)
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
<div class="hero-container reveal reveal-scale" style="{bg_style}">
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
               padding:14px 35px; border-radius:30px; color:black; font-weight:bold;">
               View Projects
            </a>
            <a href="https://linkedin.com/in/aswin" target="_blank"
               style="background:#0077b5; padding:14px 35px;
               border-radius:30px; color:white; font-weight:bold;">
               LinkedIn
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
# --------------------------------------------------
# 5. SCROLL OBSERVER (ONCE)
# --------------------------------------------------
components.html("""
<script>
document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("active");
            }
        });
    }, { threshold: 0.15 });
    document.querySelectorAll(".reveal").forEach(el => observer.observe(el));
});
</script>
""", height=0)
# --------------------------------------------------
# 6. ABOUT
# --------------------------------------------------
st.subheader("👨‍💻 About Me")
st.markdown("""
<div class="about-box reveal reveal-left">
    <p style="font-size:1.15rem; line-height:1.8;">
        Data Scientist & AI Python Trainer with a Diploma in Electronics.
        Specialized in Machine Learning, Computer Vision & Generative AI.
    </p>
</div>
""", unsafe_allow_html=True)
# --------------------------------------------------
# 7. TOOLS
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
        st.markdown('<div class="reveal reveal-scale">', unsafe_allow_html=True)
        if st.button(label, key=file, use_container_width=True):
            st.switch_page(file)
        st.markdown('</div>', unsafe_allow_html=True)
