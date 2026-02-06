import streamlit as st
import urllib.parse
# --- HEADER CONFIGURATION (PASTE THIS ON EVERY PAGE) ---
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    /* HIDE SIDEBAR & DEFAULT HEADER */
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    [data-testid="stHeader"] {display: none;}
    /* CUSTOM HEADER STYLE */
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
    .stApp { background: radial-gradient(circle at 10% 20%, rgb(10, 20, 40) 0%, rgb(5, 10, 20) 90%); color: white; }
    </style>
""", unsafe_allow_html=True)
# HEADER LAYOUT
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    st.page_link("Home.py", label="🏠 Home", use_container_width=True)
with c2:
    st.markdown('<div class="header-text">ASWIN K</div>', unsafe_allow_html=True)
with c3:
    st.link_button("📧 Contact", "mailto:contact@aswin.ai", use_container_width=True)
st.write("---")
# --- END HEADER ---
# --- APP CONTENT ---
st.title("FIND YOUR MOVIE LINKS FAST 🎬")
st.write("Experimental: Attempt to open the bot with text pre-filled.")
# 1. User Input
col1, col2 = st.columns([3, 1])
with col1:
    movie_name = st.text_input("Enter Movie Name", "")
with col2:
    year = st.text_input("Year", "")
# 2. Logic
if movie_name:
    full_query = f"{movie_name} {year}".strip()
    # Encode text for URL (Iron Man -> Iron%20Man)
    encoded_text = urllib.parse.quote(full_query)
    # --- EXPERIMENTAL METHOD: tg:// Protocol ---
    # This command tells the Telegram App specifically to:
    # 1. Resolve (Find) the bot 'StarMoviesbot'
    # 2. Fill the 'text' field with your movie name
    tg_url = f"tg://resolve?domain=StarMoviesbot&text={encoded_text}"
    st.write("---")
    st.success(f"✅ Generated for: **{full_query}**")
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{tg_url}">
            <button style="
                background: linear-gradient(45deg, #FF512F, #DD2476); 
                color: white; 
                border: none; 
                padding: 18px 40px; 
                border-radius: 50px; 
                cursor: pointer;
                font-size: 20px;
                font-weight: bold;
                box-shadow: 0 0 25px rgba(221, 36, 118, 0.6);
                transition: transform 0.2s;
                width: 100%;
            ">
                🚀 OPEN & AUTO-FILL
            </button>
        </a>
        <p style="color: #ffcccc; font-size: 14px; margin-top: 15px; background: rgba(255,0,0,0.2); padding: 10px; border-radius: 10px;">
            <b>⚠️ Important:</b> If this opens the bot but the text box is empty, it means your Telegram version has blocked Auto-Fill for bots. 
            <br>In that case, you <b>must</b> paste manually (Ctrl+V).
        </p>
    </div>
    """, unsafe_allow_html=True)
    # Backup Copy Box (Just in case the auto-fill fails)
    with st.expander("Show Manual Copy Option (If above fails)"):
        st.code(full_query, language=None)



