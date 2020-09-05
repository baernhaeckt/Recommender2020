import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class RecommenderService:

    def __init__(self) -> None:
        self.dataset = dict()
        self.results = dict()
        self.matrix = None

    def _load_data(self):
        self.dataset = pd.read_json("C:\git\BaernHaeckt\Backend2020\Data\offers.json")

    def _create_matrix(self):
        vectorizer = TfidfVectorizer(analyzer="word", stop_words="english", ngram_range=(1, 3), min_df=0)
        self.matrix = vectorizer.fit_transform(self.dataset["Description"])

    def _calculate_similarities(self):
        cosine_similarities = linear_kernel(self.matrix, self.matrix)
        for idx, row in self.dataset.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
            similar_items = [(cosine_similarities[idx][i], self.dataset["id"][i]) for i in similar_indices]
            self.results[row["id"]] = similar_items[1:]

    def _get_item(self, id):
        return self.dataset.loc[self.dataset["id"] == id]['description'].tolist()[0]
