from data_import import DataImport
from offers_recommender import RecommenderService
from config import Config
from process_launcher import ProcessLauncher

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/offers', methods=["GET"])
def recommend_offers():
    text = request.args.get("text")
    recommender = RecommenderService()
    results = recommender.recommend(text, Config.OFFERS_FILENAME)

    return jsonify(result=results)


@app.route('/paidoffers', methods=["GET"])
def recommend_paidoffers():
    text = request.args.get("text")
    recommender = RecommenderService()
    results = recommender.recommend(text, Config.PAID_OFFERS_FILENAME)

    return jsonify(result=results)


@app.route('/importoffers', methods=["GET"])
def import_offers():
    data_import = DataImport()
    dataset = data_import.create_dataset(Config.OFFERS_URL, Config.OFFERS_ROOT_ELEMENT)

    data_import.save_processsed_data(dataset, Config.OFFERS_FILENAME)

    return "Offers import finished..."


@app.route('/importpaidoffers', methods=["GET"])
def import_paid_offers():
    data_import = DataImport()
    dataset = data_import.create_dataset(Config.PAID_OFFERS_URL, Config.PAID_OFFERS_ROOT_ELEMENT)

    data_import.save_processsed_data(dataset, Config.PAID_OFFERS_FILENAME)

    return "Paid offers import finished..."


@app.route("/start", methods=["GET"])
def start_change_stream():
    ProcessLauncher()
    return "Task in progress"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")




