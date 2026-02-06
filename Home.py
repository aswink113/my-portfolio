import streamlit as st
import base64
import os
import streamlit.components.v1 as components
from PIL import Image
# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ASWIN K | AI Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --- 2. IOS GLASSMORPHISM CSS ---
st.markdown("""
    <style>
    /* 1. BACKGROUND & GLOBAL FONTS */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(10, 20, 40) 0%, rgb(5, 10, 20) 90%);
        background-attachment: fixed;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    /* HIDE DEFAULT ELEMENTS */
    [data-testid="stSidebar"] {display: none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* 2. GLASS CARD UTILITY CLASS */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        border-radius: 24px;
        padding: 30px;
    }
    /* 3. HEADER STYLING */
    .header-text {
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(90deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
        text-align: center; /* Ensures text is centered in its column */
        width: 100%;
    }
    /* 4. HERO SECTION STYLING */
    .hero-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 8rem 2rem; 
        position: relative;
        overflow: hidden;
        margin-top: 10px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    /* 5. GLASS TOOL BOXES (CLICKABLE) */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        color: #E0E0E0 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        padding: 0px; 
        height: 160px; 
        width: 100%;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    } 
    div.stButton > button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        border-color: #00ADB5 !important;
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 30px rgba(0, 173, 181, 0.25);
        color: #00ADB5 !important;
    }
    div.stButton > button p {
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0;
        letter-spacing: 0.5px;
    }
    /* 6. ABOUT ME SECTION */
    .about-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 40px;
        border-left: 4px solid #00ADB5;
    }
    </style>
""", unsafe_allow_html=True)
# --- 3. HEADER SECTION ---
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown('<div class="header-text">ASWIN K</div>', unsafe_allow_html=True)
with c2:
    st.link_button("📧 Contact Me", "mailto:aswinkandambeth113@gmail.com", use_container_width=True)
st.write("") 
# --- 4. HERO SECTION (With profile.jpg as BG) ---
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None
img_b64 = None
if os.path.exists("profile.jpg"):
    img_b64 = get_img_as_base64("profile.jpg")
bg_style = ""
if img_b64:
    bg_style = f"""
        background: linear-gradient(to right, rgba(10, 20, 40, 0.9), rgba(10, 20, 40, 0.4)), url("data:image/jpg;base64,{img_b64}");
        background-size: cover;
        background-position: center;
    """
else:
    bg_style = "background: linear-gradient(120deg, #1c1e26, #2a2d3a);"
st.markdown(f"""
<div class="hero-container" style='{bg_style}'>
    <div style="max-width: 750px; padding-left: 10px;">
        <h3 style="color: #00C9FF; margin: 0; padding: 0; letter-spacing: 3px; font-size: 18px; text-transform: uppercase;">Hello, I am an</h3>
        <h1 style="font-size: 4rem; margin: 5px 0 15px 0; font-weight: 800; background: linear-gradient(to right, #ffffff, #a0a0a0); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Data Scientist</h1>
        <p style="font-size: 1.3rem; line-height: 1.6; color: #E0E0E0; font-weight: 300;">
            I build <b>intelligent systems</b> that learn from data. Specializing in 
            <span style="color: #00C9FF; font-weight: 600;">Data Scientist       </span>   </span>       and <span style="color: #92FE9D; font-weight: 600;">Deep Learning</span> 
            to help organizations predict the future.
        </p>
        <br>
        <div style="display: flex; gap: 20px;">
            <a href="https://github.com/aswink113" target="_blank" style="background: linear-gradient(90deg, #00C9FF, #92FE9D); color: #000; padding: 14px 35px; text-decoration: none; border-radius: 30px; font-weight: bold; box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4); transition: transform 0.3s;">
                View Projects
            </a>
            <a href="https://www.linkedin.com/in/aswin-k113" target="_blank" style="background-color: #0077b5; color: white; padding: 14px 35px; text-decoration: none; border-radius: 30px; font-weight: bold; box-shadow: 0 5px 15px rgba(0, 119, 181, 0.4); transition: transform 0.3s;">
                LinkdIn
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
# --- 5. JAVASCRIPT ANIMATED STATS ---
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: transparent; }
    .stats-box {
        display: flex;
        justify-content: space-around;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 30px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        color: white;
    }
    .stat { text-align: center; }
    .number { 
        font-size: 3rem; 
        font-weight: 700; 
        background: linear-gradient(90deg, #00C9FF, #92FE9D); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        display: block; 
    }
    .label { font-size: 0.9rem; color: #aaa; margin-top: 5px; text-transform: uppercase; letter-spacing: 1px; }
</style>
</head>
<body>
<div class="stats-box" id="statsSection">
    <div class="stat"><span class="number" data-target="2.3">0</span><div class="label">Years Exp</div></div>
    <div class="stat"><span class="number" data-target="12">0</span><div class="label">Projects</div></div>
    <div class="stat"><span class="number" data-target="5">0</span><div class="label">Deployments</div></div>
    <div class="stat"><span class="number" data-target="100">0</span><div class="label">Satisfaction %</div></div>
</div>
<script>
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counters = document.querySelectorAll('.number');
                counters.forEach(counter => {
                    const target = +counter.getAttribute('data-target');
                    const duration = 1500; 
                    const increment = target / (duration / 16); 
                    let current = 0;
                    const updateCount = () => {
                        current += increment;
                        if (current < target) {
                            if (target % 1 !== 0) counter.innerText = current.toFixed(1) + "+";
                            else counter.innerText = Math.ceil(current) + "+";
                            if(target === 100) counter.innerText = Math.ceil(current) + "%";
                            requestAnimationFrame(updateCount);
                        } else {
                            if (target === 100) counter.innerText = target + "%";
                            else if (target % 1 !== 0) counter.innerText = target + "+";
                            else counter.innerText = target + "+";
                        }
                    };
                    updateCount();
                });
                observer.disconnect();
            }
        });
    });
    const target = document.querySelector('#statsSection');
    observer.observe(target);
</script>
</body>
</html>
""", height=180)
st.markdown("<br>", unsafe_allow_html=True)
# --- 6. ABOUT ME ---
st.subheader("👨‍💻 About Me")
st.markdown("""
<div class="about-box">
    <p style="font-size: 1.15rem; line-height: 1.8; color: #E0E0E0; margin: 0; font-weight: 300;">
        I am a <b>Data Scientist and AI Python Trainer</b> with a strong technical foundation built on a 
        <b>Diploma in Electronics</b>. Originally from Kannur and now based in Cochin, I specialize in transforming 
        complex data into actionable insights while mentoring the next generation of <b>AI developers</b>.
        <br><br>
        My background allows me to approach <b>Machine Learning and Computer Vision</b> with a unique engineering 
        perspective, ensuring that the <b>Python solutions</b> I build and teach are both logically sound and highly efficient.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
# --- 7. TOOL GRID ---
st.subheader("🚀 Try My AI Tools")
tools = [
    {"label": "Background Remover", "icon": "📷", "file": "pages/Background_Remover.py"},
    {"label": "AI Photo Studio", "icon": "✨", "file": "pages/AI_Photo_Studio.py"},
    {"label": "PDF Splitter", "icon": "📄", "file": "pages/PDF_Splitter.py"},
    {"label": "Object Eraser", "icon": "🧼", "file": "pages/Object_Eraser.py"},
    {"label": "Movie Link Finder", "icon": "🎬", "file": "pages/Movie_Link_Finder.py"},
    {"label": "Image Compressor", "icon": "📉", "file": "pages/Image_Compressor.py"},
]
cols = st.columns(3)
for i, tool in enumerate(tools):
    with cols[i % 3]:
        btn_label = f"{tool['icon']}\n{tool['label']}"
        if st.button(btn_label, use_container_width=True, key=tool['label']):
            if "Background" in tool['label']:
                st.switch_page("pages/Background_Remover.py")
            else:
                st.toast(f"🚧 {tool['label'].splitlines()[0]} is coming soon!", icon="🔧")
        st.write("")
