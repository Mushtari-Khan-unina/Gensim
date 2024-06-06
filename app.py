import streamlit as st
from PyPDF2 import PdfFileReader
from gensim.summarization import summarize

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    with open(uploaded_file, 'rb') as file:
        reader = PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

# Function for extractive summarization using Gensim
def extractive_summarization(text, max_words=100):
    summary = summarize(text, word_count=max_words)
    return summary

# Main Streamlit app
def main():
    st.title("PDF Summarizer")

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        # Display sample text from PDF
        sample_text = extract_text_from_pdf(uploaded_file)[:500]
        st.subheader("Sample Text from PDF:")
        st.write(sample_text)

        # Set maximum words in summary using a slider
        max_words = st.slider("Select maximum words in summary", min_value=50, max_value=500, value=100, step=50)

        # Generate summary when button is clicked
        if st.button("Summarize"):
            # Extract text from PDF
            text = extract_text_from_pdf(uploaded_file)
            
            # Generate summary
            summary = extractive_summarization(text, max_words=max_words)
            
            # Display summary
            st.subheader("Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()
