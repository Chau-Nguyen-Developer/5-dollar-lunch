from flask import Flask, render_template
from flask import request
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

# def hello_world():
#     return "<p>Hello, world!</p>"

# @app.route("/hello")
# def hello():
#     name = request. args.get("name", "Flask")
#     return f"Hello, {escape(name)} !"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'Hello User {escape(username)}. Enjoy the Full-Stack Dev.'

# @app.route('/about')
# def about():
#     return 'The About Page'

# @app.route('/projects')
# def projects():
#     return "The Projects Page"

@app.route('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Five-Dollar-Office-Gift</h1></body></html>"

data = [
    {
        "name" : "Spiral Notebook",
        "price": 3.39,
        "image_url": "https://img-1.kwcdn.com/product/open/34273584381743a98021073c1a1c725b-goods.jpeg?imageView2/2/w/264/q/70/format/avif"
    },
    {
        "name": "Monthly Calendar",
        "price": 6.99,
        "image_url": "https://img.kwcdn.com/product/open/55fee14820b34bb0b51f08bbcddc447b-goods.jpeg?imageView2/2/w/800/q/70/format/avif"

    },
    {
        "name": "Papermate Pens",
        "price": 4.89,
        "image_url": "https://target.scene7.com/is/image/Target/GUEST_adb0937c-9c7d-4665-8012-5ad39de12a81?wid=750&qlt=80"
    },
    {
        "name": "Post-it Sticky Notes",
        "price": 10.99,
        "image_url": "https://target.scene7.com/is/image/Target/GUEST_bcd05de0-9e4b-4e3b-b351-87d30e317379?wid=600&hei=600&qlt=80"
    },
    {
        "name": "Letter-Size Paper",
        "price": 5.79,
        "image_url": "https://target.scene7.com/is/image/Target/GUEST_1b8f976b-2072-422d-95f3-d747532a8de5?wid=600&hei=600&qlt=80"
    },
    {
        "name": "Paper folder",
        "price": 1.89,
        "image_url": "https://target.scene7.com/is/image/Target/GUEST_6b59a3bf-02bd-4442-aa55-c0cb0f4d6c54?wid=600&hei=600&qlt=80"
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

