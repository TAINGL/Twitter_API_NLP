"""
Mini projet Twitter

Etape 4:
Mettez sqlite et mongodb l'auteur, la date du tweet, le tweet, le nombre de mots du tweet, la liste de mots sans les stopwords

Run: python3 create_db_nosql.py
"""
from pymongo import MongoClient
import json

# Start MongoDB
#MongoClient is used to communicate with MongoDB
client = MongoClient('localhost', 27017)

db = client["twitter"]
collection = db["tweets"]
print('Database Created and Successful Connected to MongoDB')

with open('df_tweet.json') as f:
    file_data = json.load(f)

# create a gene collection and insert pubmed data 
collection.insert(file_data)
print("MongoDB table created")

collection.find_one()

client.close()
print('MongoDB connection is closed !')