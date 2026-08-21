import streamlit as st

st.set_page_config(
    page_title="AI Customer Feedback Intelligence",
    page_icon="🤓",
    layout="centered"
)

st.title("AI Customer Feedback Intelligence")

st.write(
    "Enter a customer review and the AI model will analyze the feedback."
)

review = st.text_area(
    "Customer Review",
    placeholder="Write your review here..."
)

if st.button("Analyze Review"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        st.info("Model will be connected after selecting the best model.")