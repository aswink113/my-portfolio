import streamlit as st
import sys
import os

# This block is needed so the pages folder can find utils.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Apply the style
utils.add_bg_and_footer()

# ... The rest of your existing code ...import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

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