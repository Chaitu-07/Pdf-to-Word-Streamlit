import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io

st.title("PDF to WORD Convertor")
st.write("Upload your PDF here")  

uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

if uploaded_file is not None:
    pdf = PdfReader(uploaded_file)
    st.write("PDF Successfully uploaded!")
    st.write(f"Number of pages: {len(pdf.pages)}")

    doc = Document()

    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        text = page.extract_text()
        if text:  
            doc.add_paragraph(text)

    word_io = io.BytesIO()
    doc.save(word_io)
    word_io.seek(0)

    st.download_button(
        label="Download Converted File",
        data=word_io,
        file_name="Converted.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
else:
    st.write("Please upload a PDF file")
