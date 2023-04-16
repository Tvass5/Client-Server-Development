from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37297/?authsource=AAC' % ('aacuser','turbo'))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, rData):
        # {'_id':False} just omits the unique ID of each row
        if rData:
            data = self.database.animals.find(rData,{"_id":False})
        else:
            data = self.database.animals.find( {}, {"_id":False})

        return data
    
# Create method to implement U in CRUD 
    def update (self, data, uData):
        if data is not None:
            result = self.database.animals.update_many(data, uData)
        else:
            return "{}"
        return result
    
    
# Create method to implement D in CRUD
    def delete (self, data):
        if data:
            result = self.database.animals.delete_many(data)
        else:
            return "{}"
        return result

    

    
    
     