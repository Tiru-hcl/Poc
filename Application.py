from Csv_Mongdb import db_connection,Script

if __name__ == "__main__":
    Script.count_r()
    Script.store_to_mongodb()
    Script.read_csvdata()
    #Script.store_to_mongodb()
    '''You can call this method to store records to mongodb'''


