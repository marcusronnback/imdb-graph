import json_caller
import plotSeason

def episodeRatings(seasonEp, seasonNumber, x, y):
    i = 1
    print(int(seasonNumber))
    for episode in seasonEp["Episodes"]:
        print("episode no" + str(i))
        if episode.get("Released") == "N/A":
            return
        x.append(i)
        if episode.get("imdbRating") == "N/A":
            y.append(0.0)
            print("Episode missing rating")
        else:
            y.append(float(episode.get("imdbRating")))
            print(str(i-1) + " : " + episode.get("imdbRating"))
        i = i + 1
    #plotSeason.plotSeason(seasonEp["Title"],int(seasonNumber)-1, x, y)



def main():
    x = []
    y = []
    print("Started!")
    name = input("Type the name of the Series: \n")
    (title, seasons) = json_caller.getSeriesInfo(name)
    print("\nSeasons: " + seasons)
    for season in (1, int(seasons)):
        response = json_caller.getSeasonInfo(title, season)

        print("\nResponse: \n ")
        print(response)
        print("*******************\n")
        print("Season " + response["Season"])
        episodeRatings(response, response["Season"],x,y)
        plotSeason.plotSeason(response["Title"], int(response["Season"]), x, y)
    # plotSeason.plotSeason(response["Title"], int(response["Season"]), x, y)
    # plotSeason.plotSeasons(title, episodesList, ratingsList)


if __name__ == "__main__":
    main()
