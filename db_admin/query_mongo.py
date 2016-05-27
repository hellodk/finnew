from pymongo import MongoClient
import settings

database_name = settings.DATABASE_NAME
collection_name = settings.COLLECTION_NAME
host = settings.MONGO_DB_HOST
port = settings.MONGO_DB_PORT


def get_db_connection(database_name, host, port):
    '''
    Returns database client object
    '''
    client = MongoClient(host, port)
    return client[database_name]


def insert_data(data):
    '''
    Inserts a given data into the collection
    '''
    db = get_db_connection(database_name, host, port)
    db[collection_name].insert(data)
    print "Data inserted"


def get_menu():
    '''
    Scans through mongo db and returns back
    menu to the caller
    '''
    data = []
    db = get_db_connection(database_name, host, port)
    cursor = db[collection_name].find()
    for values in cursor:
        data.append(values)
    return data
