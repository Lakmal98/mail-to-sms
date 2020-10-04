from pymongo import MongoClient
from bson.json_util import dumps

class Connection:
    def __init__(self,database):
        self.client = MongoClient('localhost:27017')#connect the mongo DB
        self.dBase = self.client[database]

    def collections(self):
        return self.dBase.list_collection_names()
    
    def find_all(self,collection):
        return dumps(self.dBase.collection.find())

