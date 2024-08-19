from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongo_client():
    uri = os.getenv("MONGODB_URI")
    return MongoClient(uri)

def store_email_in_waitlist(email):
    client = get_mongo_client()
    db_name = "langchain_demo"
    collection_name = "WaitlistEmails"
    collection = client[db_name][collection_name]
    
    # Insert email into collection
    email_data = {"email": email}
    collection.insert_one(email_data)
    return {"message": "Successfully added to waitlist!"}
