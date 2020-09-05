from data_import import DataImport
from offers_recommender import RecommenderService

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/offers', methods=["GET"])
def recommend_offers():
    text = request.args.get("text")
    recommender = RecommenderService()
    results = recommender.recommend(text)

    return jsonify(result=results)


@app.route('/import')
def import_offers():
    data_import = DataImport()
    dataset = data_import.create_dataset()

    data_import.save_processsed_data(dataset)

    return "Import finished..."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")




