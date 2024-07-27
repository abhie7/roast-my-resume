# Roat My Resume

Welcome to **Roat My Resume**, a fun and engaging web application that provides brutally honest, humorous critiques of your resume! This project is designed to help job seekers improve their resumes through light-hearted roasting while ensuring that no personal data is saved.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Upload Your Resume**: Easily upload your resume in PDF format.
- **Brutal Roasting**: Receive a humorous and constructive critique of your resume.
- **Markdown Support**: The roast is delivered in a well-formatted manner using Markdown.
- **Privacy First**: No resume data is saved or shared; your data goes poof after you leave the page.
- **User-Friendly Interface**: An intuitive and engaging interface that guides you through the process.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **PDF Parsing**: PdfMiner
- **Markdown Conversion**: marked.js (for rendering Markdown in the browser)
- **API Integration**: Groq API for generating roast responses
- **Environment Management**: dotenv for managing environment variables

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/resume-roaster.git
   cd resume-roaster
    ```
2. Set Up a Virtual Environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install Required Packages:
```bash
pip install -r requirements.txt
```
4. Set Up Environment Variables:
Create a .env file in the root directory and add your Groq API key:
```text
GROQ_API_KEY=your_api_key_here
```

## Usage
1. Start the Flask server:
```bash
python app.py
```
2. Open your web browser and navigate to `http://127.0.0.1:8080`.
3. Upload your resume in PDF format and click "Begin Roasting!" to receive your roast.

## How It Works
1. File Upload: The user uploads their resume in PDF format through the web interface.
2. PDF Parsing: The application extracts text from the uploaded PDF using a PDFminer library.
3. Resume Check: The application checks if the uploaded document is a valid resume using predefined keywords.
4. Roast Generation: If the document is a valid resume, the extracted text is sent to the Groq API, which generates a humorous roast.
5. Markdown Rendering: The roast response is converted from Markdown to HTML and displayed on the frontend.

## Disclaimer
Get Ready to Be Roasted! 🔥
By using this app, you’re signing up for a light-hearted, brutally honest roast of your resume. Expect some sass, sarcasm, and maybe a few chuckles (or gasps) as we dissect your document!
- No Feelings Hurt: It’s all in good fun!
- Your Data is Safe: No resume data will be saved or shared.
- Upload at Your Own Risk: Make sure you’re ready for the roast!
- Embrace the Roast: The more you embrace the roast, the better your resume will be!

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or open an issue.
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details. Thank you for checking out Resume Roaster! We hope you enjoy roasting your resume as much as we enjoyed creating this app. Happy job hunting! 🐔🔥
