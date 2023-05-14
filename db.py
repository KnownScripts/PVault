from pymongo import MongoClient


def get_db():
    CONNECTION_STRING = "mongodb://192.168.0.21:27017/fivem"
    client = MongoClient(CONNECTION_STRING)
    return client['VAULT']

if __name__ == "__main__":   

    # Get the database
    dbname = get_db()
