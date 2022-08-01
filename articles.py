from flask_restful import Resource

cont = {"AF": "africa", "AS": "asia", "EU": "europe"}

testData = [
  {
    "id": cont["AF"],
    "value": "Articles from Africa",
    "status": "Completed"
  },
  {
    "id": cont["AS"],
    "item": "Articles from Africa",
    "status": "Open"
  },
  {
    "id": cont["EU"],
    "item": "Articles from Europe",
    "status": "Open"
  }
]

class GetArticles(Resource):
  def get(self, id):
    for val in testData:
      if(id == val["id"]):
        return val, 200
    return "articles not found in {}".format(id), 404

#   def put(self, id):
#     for todo in todos:
#       if(id == todo["id"]):
#         todo["item"] = request.form["data"]
#         todo["status"] = "Open"
#         return todo, 200
#     return "articles not found in {}".format(id), 404