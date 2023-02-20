from flask import Flask, request
from logging import Logger

app = Flask(__name__)
log = Logger("app")

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the API playground :-)", 200

@app.route("/hello", methods=["POST", "GET"])
def hello():
    if request.method == "GET":
        # this is called short circuiting and is usually a good thing to do!
        return "Hello, User!", 200
    data = request.get_json(force=True)

    # pretty print the dictionary to see the structure
    print(data)
    if (data.get("name") is None):
        # if a name isn't in the request, return a 400.
        return None, 400
    return f"Hello, {data['name']}!", 200

