import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def load_data(path):
    return pd.read_csv(path)


def create_matrix(dataset):
    vectorizer = TfidfVectorizer(analyzer="word", stop_words="english", ngram_range=(1, 3), min_df=0)
    tfidf_matrix = vectorizer.fit_transform(dataset["description"])

    return tfidf_matrix


def calculate_similarities(matrix, data):
    cosine_similarities = linear_kernel(matrix, matrix)
    results = {}
    for idx, row in data.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], data['id'][i]) for i in similar_indices]
        results[row['id']] = similar_items[1:]

    return results


def get_item(id, data):
    return data.loc[data['id'] == id]['description'].tolist()[0].split(' - ')[0]


def recommend(item_id, num, data, results):
    item = get_item(item_id, data)
    print("Recommending " + str(num) + " products similar to " + item + "...")
    print("-------")
    recs = results[item_id][:num]

    for rec in recs:
       print("Recommended: " + get_item(rec[1], data) + " (score:" + str(rec[0]) + ")")


if __name__ == "__main__":
    dataset = load_data(".\data\sample_data.csv")
    matrix = create_matrix(dataset)
    results = calculate_similarities(matrix, dataset)

    recommend(98, 5, dataset, results)

