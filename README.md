# PDF to Word Converter

A simple and elegant Streamlit app that converts PDF files into editable Word documents (.docx).

## Features
- Upload a PDF file via a friendly web interface.
- Extracts text from each page of the PDF.
- Converts the extracted text into a Word document.
- Allows downloading the converted Word file directly.

## Tech Stack
- Python
- Streamlit for the web UI
- PyPDF2 for PDF text extraction
- python-docx for Word document creation

## How to Run
1. Use this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the app:

streamlit run app.py

## Notes
This app is designed for text-based PDFs (not scanned images).

