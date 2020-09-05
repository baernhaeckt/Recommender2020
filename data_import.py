import pandas as pd

from preprocessing import Preprocessing


class DataImport:

    def create_dataset(self):
        preprocessing = Preprocessing()
        dataset = self._load_data()
        offers = pd.DataFrame(columns=["id", "text"])

        for offer in dataset["offers"]:
            categories = " ".join(offer["Categories"])
            text = preprocessing.process_text("{0} {1} {2}".format(offer["Name"], offer["Description"], categories))

            striped_offer = [{
                "id": offer["id"],
                "text": text
            }]

            offers = offers.append(striped_offer, ignore_index=True)

        return offers

    def save_processsed_data(self, processed_data):
        processed_data.to_csv("data/offers.csv", index=False)

    def _load_data(self):
        return pd.read_json("C:\git\BaernHaeckt\Backend2020\Data\offers.json")
