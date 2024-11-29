from pymongo import MongoClient
from bson import ObjectId

uri = "mongodb+srv://lezioni:itsfoggia@cluster0.u7ews.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['project_group2']

user_collection = db.users

machinery_collection = db.machinery

plant_collection = db.plants

def toString(obj_id: ObjectId) -> str:
    return str(obj_id)

