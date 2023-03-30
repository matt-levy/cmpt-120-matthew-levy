# import the flask package for making rest apis.
from flask import Flask
from flask import *
from flask import request 
from movies import movies

# create an instance of a Flask object.
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    '''
    This is our base route. When visited, we get the text "Hello, world!"
    '''
    return "Hello, world!"

@app.route("/api/movies", methods=["GET"])
def list_movies():
    """
    This function returns a Response object back containing all
    of stored movies and reviews back to the caller on the web.
    """
    response_body = movies

    titles = request.args.getlist("title")

    # only get the movies that have the same title as the query parameter.
    if titles != []:
        response_body = [movie for movie in movies if movie["title"] in titles]

    return jsonify(response_body)

# run our application
if __name__ == '__main__':
    app.run()
