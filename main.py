#D:/full stack development/pythonProject/ptad91/ponniyin.pdf

import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, output_path="output.mp3", lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)

def convert_pdf_to_speech(pdf_path):
    # Extract text from PDF
    text = pdf_to_text(pdf_path)

    # Convert text to speech
    output_path = os.path.splitext(pdf_path)[0] + "_output.mp3"
    text_to_speech(text, output_path)

    print(f"Conversion completed. Output saved to: {output_path}")

if __name__ == "__main__":
    pdf_path = "D:/full stack development/pythonProject/ptad91/ponniyin.pdf"

    if os.path.exists(pdf_path):
        convert_pdf_to_speech(pdf_path)
    else:
        print("Invalid file path. Please provide a valid PDF file.")
