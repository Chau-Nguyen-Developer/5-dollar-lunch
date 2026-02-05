from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"
# data = [
#     {
#         "name" : "Subway",
#         "price": 8.99
#     },
#     {
#         "name": "Starbucks",
#         "price": 4.99
#     },
#     {
#         "name": "Roundtable Pizza",
#         "price": 5.99
#     },
#     {
#         "name": "Panda Express",
#         "price": 10.99
#     },
# ]

# def search_food_items(budget):
#     result = []
#     for food in data:
#         if food['price'] <= budget+2:
#             result.append(food)
#     return result

# print(search_food_items(10))