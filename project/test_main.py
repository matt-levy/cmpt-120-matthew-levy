import json
from main import app

# movies = json.loads(response.data.decode("utf-8")) turns the elements in the text file into a python list

def test_hello_world():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_list_movies():
    response = app.test_client().get("/api/movies")
    movies = json.loads(response.data.decode("utf-8"))
    assert len(movies) == 4


def test_list_movies_with_query_param():
    response = app.test_client().get("/api/movies?title=Frozen")
    movies = json.loads(response.data.decode("utf-8"))
    assert len(movies) == 1


def test_list_movies_with_query_params():
    response = app.test_client().get("/api/movies?title=Frozen&title=Moana")
    movies = json.loads(response.data.decode("utf-8"))
    assert len(movies) == 2

def test_list_movies_doesnt_contain_other_movie():
    response = app.test_client().get("/api/movies?title=Moana")
    movies = json.loads(response.data.decode("utf-8"))
    if len(movies) == 0:
        assert False
    for movie in movies:
        assert movie["title"] == "Moana"


