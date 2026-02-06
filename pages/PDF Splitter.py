import streamlit as st
# ... The rest of your existing code ...import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io
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
st.title("PDF Splitter")
uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")
if uploaded_pdf is not None:
    reader = PdfReader(uploaded_pdf)
    st.write(f"This PDF has {len(reader.pages)} pages.")
    # Input for page range
    page_selection = st.text_input("Enter page numbers to extract (e.g., 0 for first page, or 0,2 for 1st and 3rd)")
    if st.button("Split & Download"):
        if page_selection:
            try:
                writer = PdfWriter()
                selected_pages = [int(x.strip()) for x in page_selection.split(",")]
                for p in selected_pages:
                    writer.add_page(reader.pages[p])
                # Save to memory buffer
                output_pdf = io.BytesIO()
                writer.write(output_pdf)
                
                st.download_button(
                    label="Download Split PDF",
                    data=output_pdf.getvalue(),
                    file_name="split_doc.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Error: {e}. Check your page numbers.")


