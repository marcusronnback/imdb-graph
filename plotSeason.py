import matplotlib.pyplot as plotter
import math

def plotSeason(seriesTitle,seasonNumber,episodes,ratings):
    i = 0;
    s_rating = ratings[seasonNumber-1]
    for rating in s_rating:
        print(rating)
        if rating == 0.0:
            if i == 0:
                n_rating = (s_rating[i + 1] * 2) / 2
                plotter.text(i + 1, n_rating, str(n_rating), color="red")
                ratings[seasonNumber - 1][i] = n_rating
            if i == (len(ratings[seasonNumber-1])-1):
                n_rating = (s_rating[i - 1] * 2) / 2
                plotter.text(i + 1, n_rating, str(n_rating), color="red")
                ratings[seasonNumber - 1][i] = n_rating
            else:
                n_rating = (s_rating[i - 1] + s_rating[i + 1]) / 2
                plotter.text(i + 1, n_rating, str(n_rating), color="red")
                ratings[seasonNumber - 1][i] = n_rating
        else:
            plotter.text(i+1, rating, str(rating))
        i = i+1
    plotter.plot(episodes[seasonNumber-1], ratings[seasonNumber-1])
    print(str(len(episodes[int(seasonNumber)-1])) + " episodes in season " + str(seasonNumber) + " of " + seriesTitle)
    plotter.autoscale(False)
    print("**************" + str(len(episodes[int(seasonNumber)-1])) + "*******")
    plotter.axis([1, len(episodes[int(seasonNumber)-1]), 1, 10])
    plotter.title("Ratings of " + str(seriesTitle) + " Season "+ str(seasonNumber))
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


