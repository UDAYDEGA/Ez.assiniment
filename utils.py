from pdfminer.high_level import extract_text

def extract_text_from_pdf(uploaded_file):
    return extract_text(uploaded_file)

def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode('utf-8')
