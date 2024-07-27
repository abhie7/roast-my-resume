def is_resume(text):
    resume_keywords = ['Experience', 'Education', 'Skills', 'Projects', 'Certifications', 'Summary', 'gmail', 'Bachelors', 'B.tech', 'B.TECH']

    if any(keyword in text for keyword in resume_keywords):
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_resume('I have an Experience'))