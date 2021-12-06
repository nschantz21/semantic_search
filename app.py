from . import semantic_search
from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

# initialize the app
app = Flask(__name__)
run_with_ngrok(app)
api = Api(app)

# define our API end point for Semantic Search
class Query(Resource):
    # define the HTTP methods here
    def get(self, query_word):
        related_terms = semantic_search(query_word=query_word).to_dict()
        return {"related_terms": related_terms}, 200

# set the api access point to a dynamic query word 
api.add_resource(Query, "/<string:query_word>")

if __name__ == "__main__":
    app.run()
