import matplotlib.pyplot as plotter
import math

def plotSeason(seriesTitle,seasonNumber,episodes,ratings):
    plotter.plot(episodes,ratings)
    i = 0;
    for rating in ratings:
        print(rating)
        plotter.text(i+1, float(rating), float(rating))
        i = i+1

    print(str(len(episodes)) + " episodes in season " + str(seasonNumber) + " of " + seriesTitle)
    plotter.autoscale(False)
    plotter.axis([1, len(episodes), 1, 10])
    plotter.show()


def plotSeasons(seasonTitle,seasonEpisodes,ratings):
    print("Grid: "+ str(math.ceil(math.sqrt(len(seasonEpisodes)))) + "x" + str(math.ceil(math.sqrt(len(seasonEpisodes)))))
    fig, axs = plotter.subplots(math.ceil(math.sqrt(len(seasonEpisodes))), math.ceil(math.sqrt(len(seasonEpisodes))))
    for season in seasonEpisodes:
        print(season)
    for seasonNumber in range(len(seasonEpisodes)-1):
        for x in range(math.ceil(math.sqrt(len(seasonEpisodes)))):
            for y in range(math.ceil(math.sqrt(len(seasonEpisodes)))):
                print("x" + str(seasonEpisodes[seasonNumber]))
                print("y" + str(ratings[seasonNumber]))
                axs[x, y].plot(seasonEpisodes[seasonNumber], ratings[seasonNumber])
                axs[x, y].set_title("Season "+ str(seasonNumber+1) + ":")


