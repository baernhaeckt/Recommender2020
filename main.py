import nltk

from preprocessing import Preprocessing
from data_import import DataImport

from flask import Flask

app = Flask(__name__)


@app.route('/offers')
def recommend_offers():
    return "Angeln am Oeschinensee"


@app.route('/import')
def import_offers():
    data_import = DataImport()
    data_import.create_dataset()

    return "Import finished..."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")




