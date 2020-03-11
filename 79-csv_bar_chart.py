import csv
import requests
import Counter

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        return s.get(CSV_URL).text

def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    list_data = get_csv().strip().split('\n')
    list_data_split = [x.strip().split(',') for x in list_data][1:]
    timezone_counts = sorted(Counter([x[2] for x in list_data_split]).most_common())
    for zone in timezone_counts:
        spaces = 21 - len(zone[0])
        print(f'{zone[0]}{" " * spaces}| {"+" * zone[1]}')