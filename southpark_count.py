from collections import Counter, defaultdict
import csv
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')

result = defauldict(Counter)

def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    pass

possible_episodes = [str(_) for _ in range(30)]
s1 = get_season_csv_file(1)
s1_list = [line for line in s1.strip().split('\n') if line != '"']
season = s1_list[2][0]

chars = []
for line in s1_list:
    try:
        line_list = line.split(',')
        if line_list[0] == str(season):
            chars.append(line.split(",")[2])
    except:
        continue

# for char in chars:
#     try:
#         line_list = [line.split(',') for line in s1_list]
#         episode_list = [line for line in line_list if line[0] == str(season)]
#         episodes = [line[1] for line in episode_list if line[2] == char]


line_split = s1.split('\n1,')
for line in line_split:
    print(line)