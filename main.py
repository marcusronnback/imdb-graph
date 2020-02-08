import json_caller
import plotSeason

def episodeRatings(seasonEp, seasonNumber, x, y):
    i = 1
    j = 1;
    print("Season being worked on " + str(seasonNumber) + " episode " + str(j))
    #for n in range(0,len(seasonEp["Episodes"])):
        #x[int(seasonNumber)-1].append(0)
    for episode in seasonEp["Episodes"]:
        print("episode no" + str(i))
        if episode.get("Released") == "N/A":
            return
        x[int(seasonNumber)-1].append(i)
        if episode.get("imdbRating") == "N/A":
            y[int(seasonNumber)-1].append(0.0)
            print("Episode missing rating")
        else:
            y[int(seasonNumber)-1].append(float(episode.get("imdbRating")))
            print(str(i-1) + " : " + episode.get("imdbRating"))
        i = i + 1
    #plotSeason.plotSeason(seasonEp["Title"],int(seasonNumber)-1, x, y)



def main():
    x = []
    y = []
    print("Started!")
    name = input("Type the name of the Series: \n")
    (title, seasons) = json_caller.getSeriesInfo(name)
    for n in range(int(seasons)):
        x.append([])
        y.append([])
    print("\nSeasons: " + seasons)
    for season in range(1, int(seasons)+1):
        response = json_caller.getSeasonInfo(title, season)
        print("Episodes "+str(len(response["Episodes"])))
        # episodes in range(0, len(response["Episodes"])):
            #y.append([])
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
