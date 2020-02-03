from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content)
    holiday_table = soup.findAll("table", {"class": "list-table"})
    holiday_rows = holiday_table[0].find_all('tr')
    for row in holiday_rows:
        month_line = row.find('time')
        holiday_line = row.find('a')
        if month_line is not None:
            month = month_line.string.split('-')[1]
            holiday = holiday_line.string
        # print(f'{month=}')
        # print(f'{holiday=}')
            holidays[month].append(holiday.strip())
    return holidays