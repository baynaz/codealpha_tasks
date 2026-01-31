import os
import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "Mental_Health_FAQ.csv")

df = pd.read_csv(CSV_PATH, encoding="latin1")


stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)

df["processed"] = df["Questions"].apply(preprocess)

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(df["processed"])

def get_best_answer(user_question):
    user_processed = preprocess(user_question)
    user_vector = vectorizer.transform([user_processed])
    similarity = cosine_similarity(user_vector, faq_vectors)
    best_index = similarity.argmax()
    return df.iloc[best_index]["Answers"]

if __name__ == "__main__":
    print("FAQ Chatbot (mode terminal)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        answer = get_best_answer(user_input)
        print("Chatbot:", answer)
