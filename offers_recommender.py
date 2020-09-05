import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class RecommenderService:

    def recommend(self, text):
        vectorizer = TfidfVectorizer()
        dataset = self._load_data()
        similarities = list()

        for _, offer in dataset.iterrows():
            tfidf_matrix = vectorizer.fit_transform([offer["text"], text])
            similarity = (offer["id"], float((tfidf_matrix * tfidf_matrix.T).A[0, 1]))

            similarities.append(similarity)

        similarities.sort(key=lambda s: s[1], reverse=True)

        # Get all entries with a similarity greater then 0.2
        similarities = [s for s in similarities if s[1] > 0.2]

        return similarities

    def _load_data(self):
        return pd.read_csv("data/offers.csv")

    def _new(self, name, data):
        return type(name, (object,), data)
