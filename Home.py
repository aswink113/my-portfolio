import streamlit as st
from PIL import Image
import os
# --- 1. PAGE CONFIGURATION (Professional Settings) ---
st.set_page_config(
    page_title="Aswin | AI Engineer",
    layout="wide",
    initial_sidebar_state="collapsed" # Hides the sidebar by default
)
# --- 2. PROFESSIONAL CSS (Clean White & Blue Theme) ---
st.markdown("""
    <style>
    /* 1. HIDE DEFAULT STREAMLIT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;} /* Strictly hide sidebar */
    /* 2. MAIN BACKGROUND & FONTS */
    .stApp {
        background-color: #f8f9fa; /* Light Grey Background */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* 3. HEADERS */
    h1, h2, h3 {
        color: #2c3e50; /* Dark Blue-Grey */
        font-weight: 700;
    }
    /* 4. CUSTOM TOOL CARDS (The Square Boxes) */
    .tool-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); /* Subtle Shadow */
        border: 1px solid #eef0f2;
        text-align: center;
        transition: transform 0.2s;
        height: 100%;
    }
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-color: #3498db; /* Blue border on hover */
    }
    /* 5. BUTTON STYLING */
    .stButton > button {
        background-color: #3498db; /* Professional Blue */
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #2980b9; /* Darker Blue */
    }
    </style>
""", unsafe_allow_html=True)
# --- 3. HEADER / HERO SECTION ---
col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Hello, I am Aswin")
    st.markdown("### 🧠 AI Engineer & Data Scientist")
    st.markdown("""
    I build **production-grade AI systems** that solve real-world problems. 
    Specializing in Generative AI, Computer Vision, and Predictive Analytics.
    My focus is on creating clean, scalable, and efficient solutions for modern businesses.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    # Professional CTA Buttons
    b1, b2 = st.columns([1, 2])
    with b1:
        st.button("📄 Download Resume")
    with b2:
        st.button("✉️ Contact Me")
with col2:
    # Profile Image Logic
    try:
        # Looking for 'profile.jpg'
        image = Image.open("profile.jpg")
        st.image(image, use_container_width=True)
    except:
        # Fallback if image is missing
        st.warning("⚠️ Add 'profile.jpg' to folder")
        st.markdown("""
        <div style="background-color:#e0e0e0; height:300px; border-radius:15px; display:flex; align-items:center; justify-content:center;">
            <span style="color:#7f8c8d; font-size:20px;">Profile Image Placeholder</span>
        </div>
        """, unsafe_allow_html=True)
# --- 4. STATS BAR (Clean Style) ---
st.markdown("---")
s1, s2, s3, s4 = st.columns(4)
s1.metric("Experience", "1.8+ Years")
s2.metric("Projects", "12+ Completed")
s3.metric("Models Deployed", "5")
s4.metric("Client Satisfaction", "100%")
st.markdown("---")
# --- 5. "TRY MY AI TOOLS" SECTION (The Square Boxes) ---
st.markdown("## 🛠️ Try My AI Tools")
st.markdown("Explore the interactive demos below.")
st.markdown("<br>", unsafe_allow_html=True)
# List of Tools
tools = [
    {"name": "Background Remover", "icon": "📷", "desc": "Remove image backgrounds instantly using AI."},
    {"name": "AI Photo Studio", "icon": "✨", "desc": "Upscale and enhance your photos."},
    {"name": "PDF Splitter", "icon": "📄", "desc": "Extract pages from PDF documents securely."},
    {"name": "Object Eraser", "icon": "🧼", "desc": "Remove unwanted objects from images."},
    {"name": "Movie Link Finder", "icon": "🎬", "desc": "Find streaming links for your favorite movies."},
    {"name": "Image Compressor", "icon": "📉", "desc": "Reduce image size without losing quality."}
]
# Create Grid (3 columns per row)
rows = [tools[i:i + 3] for i in range(0, len(tools), 3)]
for row in rows:
    cols = st.columns(3)
    for i, tool in enumerate(row):
        with cols[i]:
            # This container simulates the card look
            with st.container(border=True):
                st.markdown(f"### {tool['icon']} {tool['name']}")
                st.write(tool['desc'])
                # NAVIGATION LOGIC
                # If the file actually exists, we link to it. 
                # If not, we show a 'Coming Soon' toast.
                if st.button(f"Launch {tool['name']}", key=tool['name']):
                    # Check if 'pages/Background_Remover.py' exists (example logic)
                    filename = tool['name'].replace(" ", "_") + ".py"
                    page_path = f"pages/{filename}"
                    if tool['name'] == "Background Remover":
                        # We know this one exists from previous steps
                        st.switch_page("pages/Background_Remover.py")
                    else:
                        st.toast(f"🚀 {tool['name']} is under construction!", icon="🚧")
    st.markdown("<br>", unsafe_allow_html=True)

