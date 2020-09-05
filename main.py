from data_import import DataImport
from offers_recommender import RecommenderService

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/offers')
def recommend_offers():
    recommender = RecommenderService()
    results = recommender.recommend("bier geniessen unterhaltung spass stadt")

    return jsonify(result=results)


@app.route('/import')
def import_offers():
    data_import = DataImport()
    dataset = data_import.create_dataset()

    data_import.save_processsed_data(dataset)

    return "Import finished..."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")




