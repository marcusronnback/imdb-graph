import json
import requests

baseurl = "http://www.omdbapi.com/?"
file = open("apikey.txt","r")
for key in file:
    apikey = key.rstrip()
print("APIkey: " + apikey)

def getSeriesInfo(n):

    question = baseurl+ "type=series&"+"t=" + n + "&plot=full" + "&apikey=" + apikey
    print(question)
    response = requests.get(question)
    print(response.json())

    with open("response3.json","w") as out:
        json.dump(response.json(),out,indent=2,separators=(',',': '))
    with open("response3.json","r") as file:
        json_dict = json.load(file)

    if "totalSeasons" in json_dict:
        return (json_dict["Title"],json_dict["totalSeasons"])
    else:
        print("No seasons exist, is it a series?")
        exit(0)

def getSeasonInfo(t,s):
    question = baseurl + "type=series" + "&t=" + str(t) + "&Season=" + str(s) + "&plot=full" + "&apikey=" + apikey
    response = requests.get(question)
    print(question)
    print(response.json())
    return response.json()