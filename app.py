import re
from pathlib import Path

import joblib
import nltk
import streamlit as st
from nltk.corpus import stopwords


st.set_page_config(
    page_title="AI Customer Feedback Intelligence",
    page_icon="🤓",
    layout="centered"
)

st.title("AI Customer Feedback Intelligence")

st.write(
    "Enter a customer review and the model will analyze the feedback."
)

base_path = Path(__file__).resolve().parent

model = joblib.load(base_path / "models" / "best_model.pkl")
vectorizer = joblib.load(base_path / "notebooks" / "tfidf_vectorizer.pkl")

try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\\s]", "", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


review = st.text_area(
    "Customer Review",
    placeholder="Write your review here..."
)

if st.button("Analyze Review"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        cleaned_review = clean_text(review)
        review_vector = vectorizer.transform([cleaned_review])

        prediction = model.predict(review_vector)[0]
        probability = model.predict_proba(review_vector)[0]
        confidence = probability.max() * 100

        if prediction == 1:
            st.success("Recommended")
        else:
            st.error("Not Recommended")

        st.write(f"Confidence: {confidence:.2f}%")