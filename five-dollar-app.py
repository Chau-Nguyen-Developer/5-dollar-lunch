from flask import Flask, render_template
from flask import request
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    
# def hello_world():
#     return "<p>Hello, world!</p>"

@app.route("/hello")
def hello():
    name = request. args.get("name", "Flask")
    return f"Hello, {escape(name)} !"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hello User {escape(username)}. Enjoy the Full-Stack Dev.'

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/projects')
def projects():
    return "The Projects Page"

@app.route('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Five-Dollar-Office-Gift</h1></body></html>"

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
@app.route('/search/<budget>')
def search_gift_items(budget):
    # The given budget is a string. We have to convert it to float data type. 
    budget = float(budget)
    result = []
    for gift in data:
        if gift['price'] <= budget+2:
            result.append(gift)
    print (result)
    return result

print(search_gift_items(10))

