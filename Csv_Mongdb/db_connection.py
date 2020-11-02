import pymongo
def db_detaisl():
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['tiru']  # Replace with your db name
    collection_name = 'test'  # Replace with your  collection name
    db_cm = mng_db[collection_name]
    return db_cm