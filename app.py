from flask import Flask, render_template, request, jsonify
from utils.pdf_parser import parse_pdf
from utils.resume_checker import is_resume
from groq_api.groq_api import generate_roast
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return jsonify({'roast_message': "No file part in the request."})
        resume_file = request.files['resume']
        if resume_file.filename == '':
            return jsonify({'roast_message': "No selected file."})
        resume_text = parse_pdf(resume_file)
        filename = resume_file.filename
        if is_resume(resume_text):
            roast_message = generate_roast(resume_text)
        else:
            roast_message = "This is not a resume. You thought I would break if you uploaded something other than a resume, huh? The dev (Abhie) kept this in mind for blokes like you! 😎"
            logger.info(f'Filename: {filename} was uploaded and was not a resume.')
        # roast_message = generate_roast(resume_text)
        return jsonify({'roast_message': roast_message})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)