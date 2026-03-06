from flask import Flask, render_template, jsonify
from flask import request
from markupsafe import escape


# =================================
# Connect to MongoDB data base

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os
import certifi
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["five-dollar"]           # the name of database
collection = db["gift-collection"]   # the name of collection

for gift in collection.find():
    print(gift["name"])


# ================================
# import mongo_test
# collection = mongo_test.collection
# =================================

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Five-Dollar-Office-Gift</h1></body></html>"



@app.route('/search/<budget>')
def search_gift_items(budget):
    # The given budget is a string. We have to convert it to float data type. 
    budget = float(budget)

    result = []

    for item in collection.find({"price": {"$lte": budget+2}}): # lte: less than or equal
        item["_id"] = str(item["_id"]) 
        result.append(item)
        
    return jsonify(result)

# Include these two lines to be able to run from python five_dollar_app.py
if __name__ == "__main__":
    app.run(debug=True)

