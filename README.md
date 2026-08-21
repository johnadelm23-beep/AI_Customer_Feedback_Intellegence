# AI Customer Feedback Intelligence

A simple Machine Learning project for analyzing customer reviews and predicting whether a customer recommends a product or not.

## Project Idea

The project uses customer review data and Natural Language Processing (NLP) techniques to convert text into numerical features. Different Machine Learning models are trained and compared using the same preprocessing and train/test split.

## Dataset

The project uses the **Women's Clothing E-Commerce Reviews** dataset.

The main fields used in the project include:
- Review Text
- Rating
- Recommended IND
- Positive Feedback Count

`Recommended IND` is used as the target for the classification models.

## Project Workflow

1. Data Cleaning and EDA
2. NLP Text Preprocessing
3. TF-IDF Feature Extraction
4. Train/Test Split
5. Model Training
6. Model Comparison
7. K-Means Clustering
8. Streamlit Deployment

## Models

Five classification models are used:

- Logistic Regression
- Random Forest
- Multinomial Naive Bayes
- SVC
- Decision Tree

K-Means is also used separately to cluster similar customer reviews.

## Model Evaluation

The classification models are compared using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The best model is selected based on the final comparison.

## Best Model

The current best overall model is **Logistic Regression**.

- Accuracy: 92.48%
- Precision: 93.08%
- F1 Score: 95.84%

SVC achieved the highest Recall at 99.97%.

## Streamlit Application

The final model is connected to a simple Streamlit application.

The user enters a customer review, then the application:

1. Cleans the review text
2. Converts it using the saved TF-IDF vectorizer
3. Sends it to the trained model
4. Displays Recommended or Not Recommended
5. Displays the prediction confidence

## Project Structure

```text
AI_Customer_Feedback_Intellegence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── nlp_preprocessing.ipynb
│   ├── logistic_regression.ipynb
│   ├── random_forest.ipynb
│   ├── naive_bayes.ipynb
│   ├── SVC_Model.ipynb
│   ├── decision_tree.ipynb
│   ├── k_means_clustring.ipynb
│   └── model_comparison.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

## Run the Application

Install the required packages:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

## Team Members

- John Adel
- Abdelrahman Ashraf
- Amr Yasser
- Bassem Ahmed
- Sayed Ragab
