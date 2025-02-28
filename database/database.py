from pymongo import MongoClient
import os

# Load MongoDB connection URL from an environment variable or config
MONGO_URI = os.getenv("MONGO_URI", "mongodb://username:password@host:port/database")

# Create MongoDB client
client = MongoClient(MONGO_URI)

# Select the database (change 'your_database_name' to your actual DB name)
db = client["your_database_name"]

print("Connected to MongoDB:", db.name)

# Define collections (equivalent to SQL tables)
thumbnails = db["thumbnails"]
settings = db["settings"]

# Function to add a thumbnail
def add_thumb(id, msg_id):
    thumbnails.update_one({"_id": id}, {"$set": {"msg_id": msg_id}}, upsert=True)

# Function to delete a thumbnail
def del_thumb(id):
    thumbnails.delete_one({"_id": id})

# Function to get a thumbnail
def get_thumb(id):
    return thumbnails.find_one({"_id": id})

# Function to update settings
def update_setting(id, value):
    settings.update_one({"_id": id}, {"$set": {"value": value}}, upsert=True)

# Function to get a setting
def get_setting(id):
    return settings.find_one({"_id": id})
    
