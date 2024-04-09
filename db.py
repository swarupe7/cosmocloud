from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://20pa1a05e7:20pa1a05e7@cluster0.d09bu1x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["library_management"]  
students_collection = db["students"] 


