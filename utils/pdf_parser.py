import pdfminer.high_level
from werkzeug.datastructures import FileStorage
import re

def parse_pdf(file):
    if isinstance(file, FileStorage):
        file = file.stream
    text = pdfminer.high_level.extract_text(file)

    text = re.sub(r"(\n+)", "", text)
    text = re.sub(r"[^\w\s/@]", '', text)
    text = re.sub(r"(\s){2,}", " ", text)
    text = re.sub(r"[•\t▪➢❖\-\/]", '', text)
    return text.strip()

if __name__ == '__main__':
    with open('./test/Keyan’s resume.pdf', 'rb') as f:
        print(parse_pdf(f))