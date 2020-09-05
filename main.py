from flask import Flask

app = Flask(__name__)


@app.route('/offers')
def recommend_offers():
    return "Angeln am Oeschinensee"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")




