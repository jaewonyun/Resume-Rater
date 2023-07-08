# %%
import pytesseract
from pdf2image import convert_from_path
import docx
import os
import os
import pandas as pd
import openai

import json
import re
#%%
def pdf_to_images(pdf_path):
    return convert_from_path(pdf_path)

def ocr_image(image):
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_path):
    images = pdf_to_images(pdf_path)
    text = ""

    for image in images:
        text += ocr_image(image)

    return text


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text



def extract_text_from_resume(file_path):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Depending on the file extension, call the right function
    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file type"



def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

### Read Python string into Python list of dictionaries

def read_string_to_list(input_string):
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\"")  # Replace single quotes with double quotes for valid JSON
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None   



