import pandas as pd

from preprocessing import Preprocessing


class DataImport:

    def create_dataset(self, data_url):
        preprocessing = Preprocessing()
        dataset = self._load_data(data_url)
        offers = pd.DataFrame(columns=["id", "text"])

        for offer in dataset["offers"]:
            categories = " ".join(offer["categories"])
            text = preprocessing.process_text("{0} {1} {2}".format(offer["name"], offer["description"], categories))

            striped_offer = [{
                "id": offer["id"],
                "text": text
            }]

            offers = offers.append(striped_offer, ignore_index=True)

        return offers

    def save_processsed_data(self, processed_data, filename):
        processed_data.to_csv("data/{0}".format(filename), index=False)

    def _load_data(self, data_url):
        return pd.read_json(data_url)
