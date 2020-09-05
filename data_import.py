import pandas as pd


class DataImport:

    def create_dataset(self):
        dataset = self._load_data()
        offers = pd.DataFrame(columns=["id", "text"])

        for offer in dataset["offers"]:
            categories = " ".join(offer["Categories"])
            print(categories)
            striped_offer = [{
                "id": offer["id"],
                "text": "{0} {1} {2}".format(offer["Name"], offer["Description"], categories)
            }]

            offers = offers.append(striped_offer, ignore_index=True)

        return offers

    def save_processsed_data(self, processed_data):
        processed_data.to_csv("offers.csv", index=False)

    def _load_data(self):
        return pd.read_json("C:\git\BaernHaeckt\Backend2020\Data\offers.json")
