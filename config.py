class Config:
    OFFERS_URL = "https://baernhaeckt2020.azurewebsites.net/api/Offers"
    PAID_OFFERS_URL = "https://baernhaeckt2020.azurewebsites.net/api/PaidOffers"

    OFFERS_FILENAME = "offers.csv"
    PAID_OFFERS_FILENAME = "paidoffers.csv"

    SIMILARITY_THRESHOLD = 0.2

    OFFERS_ROOT_ELEMENT = "offers"
    PAID_OFFERS_ROOT_ELEMENT = "paidOffers"

    MONGODB_CONNECTION_STRING = "mongodb://baernhaeckt2020:RjAMch5WH41nxzej3mr6lxGwHVCHN7stC4joHB35uBwmUbmMBliUdRxicle7H0K2ShgekM2UF37ySqkKwTq05A==@baernhaeckt2020.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@baernhaeckt2020@"
