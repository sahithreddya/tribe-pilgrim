from flask_restful import Resource
from ContinentCall import ContinentCall

cont = {"AF": "africa", "AS": "asia", "EU": "europe","NA": "north-america","SA":"south-america","AUS":"australia"}

testData = [
  {
    "id": cont["AF"],
    "item": "Articles from Africa",
    "status": "Completed"
  },
  {
    "id": cont["AS"],
    "item": "Articles from Asia",
    "status": "Open"
  },
  {
    "id": cont["EU"],
    "item": "Articles from Europe",
    "status": "Open"
  },
  {
    "id": cont["NA"],
    "item": "Articles from North America",
    "status": "Open"
  },
  {
    "id": cont["SA"],
    "item": "Articles from South America",
    "status": "Open"
  },
  {
    "id": cont["AUS"],
    "item": "Articles from Australia",
    "status": "Open"
  }
]

continent = ContinentCall(input)

class GetArticles(Resource):
  def get(self, id):
    geo = continent.region(id)
    for val in testData:
      if(id == val["id"]):
        return geo, 200
    return "articles not found in {}".format(id), 404