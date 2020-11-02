import csv

from Csv_Mongdb import db_connection
def count_r():
    '''This function will count records in dvb collection'''
    ccc = db_connection.db_detaisl().find().count()
    print(ccc)

def sort_r(field):
    '''This function will retrieve records from db in sorted manner'''
    cd = db_connection.db_detaisl().find().sort(field,1)
    for s_r in cd:
        print(s_r)


def read_csvdata():
    '''This function read csv file and return generator object'''
    with open("E:/db/100000_Sales_Records.csv",'r') as a:
        cs_r = csv.DictReader(a)
        yield cs_r

def store_to_mongodb():
    '''This function will store each record to mongodb db'''
    for each in read_csvdata():
        for each_rec in each:
            db_connection.db_detaisl().insert(each_rec)

def using_pandas():
    pass



