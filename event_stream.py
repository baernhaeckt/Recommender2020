import pymongo
import pandas as pd

from preprocessing import Preprocessing
from config import Config


class EventStream:
    def watch(self):
        uri = Config.MONGODB_CONNECTION_STRING
        client = pymongo.MongoClient(uri)
        db = client.Prod

        while True:
            change_stream = db.offers.watch([
                {
                    "$match": {
                        "operationType": {"$in": ["insert", "update", "replace"]}
                    },
                },
                {
                    "$project": {"_id": 1, "fullDocument": 1, "ns": 1, "documentKey": 1}
                }],
                "updateLookup")

            for change in change_stream:
                self.process_changes(change)

    def process_changes(self, change):
        document = change.get("fullDocument")
        document_id = document.get("_id")

        preprocessing = Preprocessing()
        categories = " ".join(list(document.get("Categories")))
        text = preprocessing.process_text(
            "{0} {1} {2}".format(document.get("Name"), document.get("Description"), categories)
        )

        dataset = pd.read_csv("data/{0}".format(Config.OFFERS_FILENAME))
        dataset.at[dataset["id"] == str(document_id), "text"] = text

        dataset.to_csv("data/{0}".format(Config.OFFERS_FILENAME), index=False)
