import pymongo

#define function to make mongo configs 
def mongo_configs():
    mongoClient = pymongo.MongoClient('127.0.0.1:27017')
    tododb = mongoClient['tododb']
    todoCollection = tododb['tasks']
    #retur a collection object 
    return todoCollection 

if __name__ == "__main__":
    print("hello")