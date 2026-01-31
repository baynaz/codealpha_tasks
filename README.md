# CodeAlpha AI Tasks  
**Intern:** Zaynab Merimi

---

## Overview  
This repository contains **AI projects completed as part of the CodeAlpha internship**, demonstrating practical applications of AI. 
Tasks 1 and 2 have been implemented and deployed via Streamlit.

---

## Tasks Completed  

### ✅ Task 1: Language Translation Tool  
- User interface to enter text and select source & target languages.  
- Uses translation APIs (Google Translate or Microsoft Translator) to process input.  
- Displays translated text clearly on the screen.   

### ✅ Task 2: Chatbot for FAQs  
- Collects FAQs related to a topic or product.  
- Preprocesses text using NLP libraries (NLTK / SpaCy).  
- Matches user questions with the most similar FAQ using cosine similarity.  
- Displays best-matching answers in a simple chatbot interface.  

---

## Deployment  
Both tasks are deployed on Streamlit: 
**Task_1 Deployed on: [https://ai-learning-portfolio-a69txdtl5wdjgjqdmfkpyb.streamlit.app/](https://ai-learning-portfoliogit-kuvolza33sundtzxstrqel.streamlit.app/)**  
**Task_2 Deployed on: [https://ai-learning-portfolio-a69txdtl5wdjgjqdmfkpyb.streamlit.app/](https://ai-learning-portfolio-a69txdtl5wdjgjqdmfkpyb.streamlit.app/)** 

---

## How to Run Locally  

1. Clone this repository:  
```bash
git clone https://github.com/baynaz/codealpha_tasks.git
```
2. Navigate to the project folder:
```bash
cd codealpha_tasks
```

3. Install dependencies & run the translator app:
```bash
cd translator
pip install -r requirements.txt
streamlit run translator/main.py  
```

4. Install dependencies & run the chatbot app:
```bash
cd faq
pip install -r requirements.txt
streamlit run faq/chatbot_app.py
```
