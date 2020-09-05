import pandas as pd


class DataImport:

    def create_dataset(self):
        dataset = self._load_data()
        for offer in dataset["offers"]:
            print(offer["Description"])

    def _load_data(self):
        return pd.read_json("C:\git\BaernHaeckt\Backend2020\Data\offers.json")
