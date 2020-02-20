import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean
from operator import itemgetter

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

filename = local
filename = 'movie_metadata.csv'

def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    res = {}
    with open(filename, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            movie_details = Movie(row['movie_title'],
                                  row['title_year'],                  
                                  float(row['imdb_score']))
            if row['director_name'] in res:
                res[row['director_name']].append(movie_details)
            else:
                res[row['director_name']] = [movie_details]
    return res


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(mean([x.score for x in movies]), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    d_with_max = [director for director in directors if len(directors[director]) >= MIN_MOVIES]
    av_directors = [(d, calc_mean_score(directors[d])) for d in d_with_max]
    return sorted(av_directors, key=itemgetter(1), reverse=True)