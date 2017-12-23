# restaurantes/models.py
from pymongo import MongoClient

client = MongoClient()
db = client.test
restaurantes = db.restaurants
