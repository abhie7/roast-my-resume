from flask import Flask, render_template, request, jsonify
from utils.pdf_parser import parse_pdf
from utils.resume_checker import is_resume
from groq_api.groq_api import generate_roast
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

load_dotenv()
MONGO_CONNECTION_STRING = os.getenv('MONGO_URI')

# Connect to MongoDB database
client = MongoClient(MONGO_CONNECTION_STRING)
db = client['roast_my_resume_db']
collection = db['resume_roast_responses']

try:
    client.admin.command('ping')
    logger.info("Connected to MongoDB Atlas.")
except Exception as e:
    logger.info(f'Could not connect to MongoDB: {e}')

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
            # Store the data in MongoDB
            data = {
                'file_name': filename,
                'resume_text': resume_text,
                'llm_response': roast_message,
                'upload_date': datetime.datetime.now()
            }
            try:
                collection.insert_one(data)
                print(f'\nCreated {filename} object to MongoDB Atlas.')
                logger.info(f"Created {filename} object to MongoDB Atlas.")
            except Exception as e:
                logger.error(f'Failed to insert data into MongoDB: {e}')
                return jsonify({'roast_message': "Failed to generate response. Please try again."}),500
        else:
            roast_message = "This is not a resume. You thought I would break if you uploaded something other than a resume, huh? The dev (Abhie) kept this in mind for blokes like you! 😎"
        # roast_message = generate_roast(resume_text)
        return jsonify({'roast_message': roast_message})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)