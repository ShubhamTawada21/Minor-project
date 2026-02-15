import streamlit as st
import PyPDF2
import random

st.set_page_config(page_title="Offline Subjective Question Generator")

st.title("📘 Offline Subjective Question Generator from PDF")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

def extract_text(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def generate_questions(text):
    sentences = text.split(".")
    questions = []

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence.split()) > 8:
            questions.append("Explain in detail: " + sentence)

    random.shuffle(questions)
    return questions[:10]

if uploaded_file:
    text = extract_text(uploaded_file)

    if st.button("Generate Subjective Questions"):

        if len(text.strip()) == 0:
            st.warning("PDF contains no readable text.")
        else:
            questions = generate_questions(text)

            st.subheader("📖 Subjective Questions")

            for i, q in enumerate(questions, 1):
                st.write(f"{i}. {q}")