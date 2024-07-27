import pdfminer.high_level
from werkzeug.datastructures import FileStorage

def parse_pdf(file):
    if isinstance(file, FileStorage):
        file = file.stream
    text = pdfminer.high_level.extract_text(file)
    return text

if __name__ == '__main__':
    with open('./test/Abhiraj_AIML_Resume_April24.pdf', 'rb') as f:
        print(parse_pdf(f))