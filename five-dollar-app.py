from flask import Flask
from flask import request
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

@app.route("/hello")
def hello():
    name = request. args.get("name", "Flask")
    return f"Hello,{escape(name)} !"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/projects')
def projects():
    return "The Projects Page"
    
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