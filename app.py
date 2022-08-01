from flask import Flask
from flask_restful import Api

from articles import GetArticles

app = Flask(__name__)
api = Api(app)

api.add_resource(GetArticles, "/articles/<string:id>")

if __name__ == "__main__":
  app.run()