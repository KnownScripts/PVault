from pymongo import MongoClient


def get_db():
    CONNECTION_STRING = "mongodb://192.168.0.21:27017/?authMechanism=DEFAULT/fivem"
    client = MongoClient(CONNECTION_STRING)
    return client['users']

if __name__ == "__main__":   

    # Get the database
    dbname = get_db()
