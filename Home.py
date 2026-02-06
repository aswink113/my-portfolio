import streamlit as st
import base64
import os
import streamlit.components.v1 as components
# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ASWIN K | AI Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --- 2. CSS STYLING ---
st.markdown("""
    <style>
    /* GLOBAL FONTS & BACKGROUND */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(10, 20, 40) 0%, rgb(5, 10, 20) 90%);
        background-attachment: fixed;
        color: white;
    } 
    /* HIDE SIDEBAR & HEADER ELEMENTS */
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    footer {visibility: hidden;}
    /* HEADER TEXT STYLING */
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
    /* TOOL GRID BUTTONS */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        color: white;
        height: 140px; 
        width: 100%;
        transition: 0.3s;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    div.stButton > button:hover {
        border-color: #00ADB5;
        transform: translateY(-5px);
        color: #00ADB5;
    }
    div.stButton > button p {
        font-size: 1.2rem;
        font-weight: 600;
    }
    /* HERO SECTION */
    .hero-container {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 5rem 2rem;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)
# --- 3. THE HEADER ---
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    st.page_link("Home.py", label="🏠 Home", use_container_width=True)
with c2:
    st.markdown('<div class="header-text">ASWIN K</div>', unsafe_allow_html=True)
with c3:
    st.link_button("📧 Contact Me", "mailto:contact@aswin.ai", use_container_width=True)
st.write("") 
# --- 4. HERO SECTION ---
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
    bg_style = f"""background: linear-gradient(to right, rgba(10, 20, 40, 0.95), rgba(10, 20, 40, 0.5)), url("data:image/jpg;base64,{img_b64}"); background-size: cover; background-position: center;"""
else:
    bg_style = "background: linear-gradient(120deg, #1c1e26, #2a2d3a);"
st.markdown(f"""
<div class="hero-container" style='{bg_style}'>
    <div style="max-width: 700px;">
        <h3 style="color: #00C9FF; margin:0;">HELLO, I AM A</h3>
        <h1 style="font-size: 3.5rem; margin: 10px 0;">Data Scientist</h1>
        <p style="font-size: 1.2rem; color: #E0E0E0;">
            I build <b>intelligent systems</b> that learn from data. Specializing in 
            <b>Generative AI</b> and <b>Deep Learning</b>.
        </p>
        <br>
        <div style="display: flex; gap: 15px;">
             <a href="https://github.com/aswin" target="_blank" style="background: linear-gradient(90deg, #00C9FF, #92FE9D); color: #000; padding: 12px 25px; text-decoration: none; border-radius: 30px; font-weight: bold;">View Projects</a>
             <a href="https://www.linkedin.com/in/aswin" target="_blank" style="background-color: #0077b5; color: white; padding: 12px 25px; text-decoration: none; border-radius: 30px; font-weight: bold;">LinkedIn</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
# --- 5. STATS ---
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; font-family: sans-serif; background: transparent; }
    .stats-box { display: flex; justify-content: space-around; color: white; flex-wrap: wrap; }
    .stat { text-align: center; margin: 10px; }
    .number { 
        font-size: 2.5rem; font-weight: 700; 
        background: linear-gradient(90deg, #00C9FF, #92FE9D); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        display: block; 
    }
    .label { font-size: 0.8rem; color: #aaa; margin-top: 5px; text-transform: uppercase; }
</style>
</head>
<body>
<div class="stats-box">
    <div class="stat"><span class="number">2.3+</span><div class="label">Years Exp</div></div>
    <div class="stat"><span class="number">12+</span><div class="label">Projects</div></div>
    <div class="stat"><span class="number">5+</span><div class="label">Deployments</div></div>
    <div class="stat"><span class="number">100%</span><div class="label">Satisfaction</div></div>
</div>
</body>
</html>
""", height=120)
st.markdown("<br>", unsafe_allow_html=True)
# --- 6. ABOUT ME ---
st.subheader("👨‍💻 About Me")
st.markdown("""
<div style="background: rgba(255, 255, 255, 0.03); padding: 30px; border-radius: 20px; border-left: 4px solid #00ADB5;">
    <p style="font-size: 1.15rem; line-height: 1.8; color: #E0E0E0; margin: 0;">
        I am a <b>Data Scientist and AI Python Trainer</b> with a strong technical foundation built on a 
        <b>Diploma in Electronics</b>. Originally from Kannur and now based in Cochin, I specialize in transforming 
        complex data into actionable insights while mentoring the next generation of <b>AI developers</b>.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
# ... (Keep all your CSS and Header code the same) ...

# --- 7. TOOLS GRID (Page Name Method) ---
st.subheader("🚀 Try My AI Tools")

# UPDATED: We removed "pages/" and ".py". Streamlit sometimes prefers just the name.
tools = [
    {"label": "Background Remover", "icon": "📷", "page": "Background_Remover"},
    {"label": "AI Photo Studio", "icon": "✨", "page": "AI_Photo_Studio"},
    {"label": "PDF Splitter", "icon": "📄", "page": "PDF_Splitter"},
    {"label": "Object Eraser", "icon": "🧼", "page": "Object_Eraser"},
    {"label": "Movie Link Finder", "icon": "🎬", "page": "Movie_Link_Finder"},
    {"label": "Image Compressor", "icon": "📉", "page": "Image_Compressor"},
]

cols = st.columns(3)

for i, tool in enumerate(tools):
    with cols[i % 3]:
        if st.button(f"{tool['icon']}\n{tool['label']}", use_container_width=True, key=tool['label']):
            try:
                # Try switching by the simple page name
                st.switch_page(f"pages/{tool['page']}.py")
            except:
                try:
                    # Backup: Try switching without the folder path
                    st.switch_page(f"{tool['page']}")
                except:
                    st.error(f"Still can't find {tool['page']}. Did you Reboot?")
