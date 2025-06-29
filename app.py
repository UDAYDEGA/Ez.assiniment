
import os
print("Current directory:", os.getcwd())
import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_txt
from summarizer import get_summary
from qa_engine import answer_question
from challenge_mode import generate_questions, evaluate_answer

st.set_page_config(page_title="📘 Smart Assistant", layout="wide")
st.title("📘 Smart Assistant for Research Summarization")

# Upload section
uploaded_file = st.file_uploader("📤 Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    # Detect file type and extract text
    if uploaded_file.type == "application/pdf":
        document_text = extract_text_from_pdf(uploaded_file)
    else:
        document_text = extract_text_from_txt(uploaded_file)

    # Display Summary
    st.subheader("📄 Document Summary:")
    with st.spinner("Generating summary..."):
        summary = get_summary(document_text)
        st.write(summary)

    # Mode selection
    st.subheader("🧠 Choose Interaction Mode")
    mode = st.radio("Select Mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        st.info("You can ask any question about the uploaded document.")
        user_question = st.text_input("❓ Ask your question:")
        if user_question:
            with st.spinner("Thinking..."):
                answer = answer_question(document_text, user_question)
                st.success(f"🗣️ Answer: {answer}")

    elif mode == "Challenge Me":
        st.info("We will generate 3 questions. Try to answer them!")
        with st.spinner("Generating questions..."):
            generated = generate_questions(document_text)
            questions = generated.split('\n')[:3]

        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}: {q}**")
            user_input = st.text_input(f"Your Answer {i+1}")
            if user_input:
                correct_answer = "Answer from doc (add logic)"  # You can improve this logic
                feedback = evaluate_answer(user_input, correct_answer)
                st.write(f"Feedback: {feedback}")

else:
    st.warning("📁 Please upload a document to begin.")
