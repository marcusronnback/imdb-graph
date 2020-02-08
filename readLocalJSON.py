import json
import plotSeason

#file = open("response.json","r")
#parsed = json.load(file)
#dump = json.dumps(parsed,indent=2, sort_keys=True)
#print(dump)
episodes = dict()
def main():
    noSeason = numOfSeasons()
    noOfEpisodes = noOfEpisodesInSeason(1)
    print()

def numOfSeasons():
    with open("response.json","r") as file:
        json_dict = json.load(file)

    if "totalSeasons" in json_dict:
        print("exists")
        print(json_dict["totalSeasons"])
        return json_dict["totalSeasons"]

def noOfEpisodesInSeason(n):

    with open("response1.json","r") as file:
        json_dict = json.load(file)
        x = [0]
        y = [0]
        for episode in json_dict["Episodes"]:
            x.append(int(episode.get("Episode")))
            y.append(float(episode.get("imdbRating")))
            print(episode.get("Episode") + " : " + episode.get("imdbRating"))
        s = 1 # season number
        plotSeason.plotSeason(s,x,y)

    return (len(json_dict["Episodes"]))




if __name__ == "__main__":
    main()