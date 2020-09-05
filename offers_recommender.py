import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class RecommenderService:

    def recommend(self, text):
        vectorizer = TfidfVectorizer(ngram_range=(1, 3), min_df=0)
        dataset = self._load_data()
        similarities = list()

        print(dataset)
        for _, offer in dataset.iterrows():
            tfidf_matrix = vectorizer.fit_transform([offer["text"], text])
            similarity = {"id": offer["id"], "similarity": (tfidf_matrix * tfidf_matrix.T).A[0, 1]}

            similarities.append(similarity)

        return similarities

    def _load_data(self):
        return pd.read_csv("data/offers.csv")
