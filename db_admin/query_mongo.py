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


def insert_data(data, database_name, collection_name):
    '''
    Inserts a given data into the collection
    '''
    db = get_db_connection(database_name, host, port)
    db[collection_name].insert(data)



