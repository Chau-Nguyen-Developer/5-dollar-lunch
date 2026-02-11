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
    
data = [
    {
        "name" : "Spiral Notebook",
        "price": 3.39
    },
    {
        "name": "Monthly Calendar",
        "price": 6.99
    },
    {
        "name": "Papermate Pens",
        "price": 4.89
    },
    {
        "name": "Post-it Sticky Notes",
        "price": 10.99
    },
    {
        "name": "Letter-Size Paper",
        "price": 5.79
    },
    {
        "name": "Paper folder",
        "price": 1.89
    },
]
@app.route('/<budget>')
def search_gift_items(budget):
    result = []
    for gift in data:
        if gift['price'] <= budget+2:
            result.append(gift)
    return result

print(search_gift_items(10))

