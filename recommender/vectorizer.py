from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def train_vectorizer(texts):
    vectorizer = TfidfVectorizer(
        max_features=7000,
        ngram_range=(1, 2),
        stop_words="english"
    )
    vectors = vectorizer.fit_transform(texts)
    return vectorizer, vectors

def save_vectorizer(vectorizer, path="vectorizer.pkl"):
    joblib.dump(vectorizer, path)

def load_vectorizer(path="vectorizer.pkl"):
    return joblib.load(path)
