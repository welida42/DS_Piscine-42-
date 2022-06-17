#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup
import requests
import time



def ft_env(ticker, field):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    h = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=h)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.title.string == "Symbol Lookup from Yahoo Finance":
        raise Exception("invalid ticker name")
    raw = soup.find('span', string=field)
    #print(soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text)
    import re
    # for tag in soup.find_all("div", attrs={'title': field}):
    #     print(tag.text)
    data = soup.find(attrs={'title': field})
    if data is None:
        raise Exception("invalid field name")
    row = data.find_parent(attrs={'data-test': "fin-row"})  # table
    children = row.find().children
    res = []
    for i in children:
        res.append(i.find("span").text)
    print(tuple(res))
    time.sleep(5)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise Exception("invalid argument count")
        ft_env(sys.argv[1], sys.argv[2])
    except Exception as e:
        print("Error:", e)