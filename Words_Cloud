import streamlit as st
from PyPDF2 import PdfReader
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to read PDF
def read_pdf(file):
    pdfReader = PdfReader(file)
    text = ""
    for page_num in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[page_num]
        text += pageObj.extract_text()
    return text

# Streamlit app
st.title("PDF to Word Cloud Generator - JRao")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("File uploaded. Click the button to generate the word cloud.")
    if st.button("Generate"):
        text = read_pdf(uploaded_file)
        
        # Generate word cloud
        wordcloud = WordCloud().generate(text)

        # Create a figure and axis
        fig, ax = plt.subplots()
        
        # Display the generated word cloud
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        
        # Show the plot using Streamlit
        st.pyplot(fig)
