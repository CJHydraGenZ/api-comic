
from turtle import title
import httpx
from bs4 import BeautifulSoup
from typing import Union

from fastapi import FastAPI
import requests
import os
import urllib.request

url = 'https://komikcast.me/'
# # r = 'hello world'


# def getData(url):
#     r = httpx.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     print(soup)
#     return soup


# # def getNextPage(soup):


# getData(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://google.com',
    'DNT': '1',
    'Cahya': 'sahhda'
}
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/comic/")
def read_item():
    r = httpx.get(url, headers=headers)
# print(r)
    soup = BeautifulSoup(r.content, 'html.parser')
# # for list_upt in soup.find_all('div', class_='utao')
# # l = soup.select('.listupd')
    data = []

    # data = [list for list in soup.find_all('div', class_='utao')]
    # thumb = data.img['src']
    # title = data.h3.text

    for list in soup.find_all('div', class_='utao'):
        thumb = list.img['src']
        title = list.h3.text
        # ch = list.li.a.text
        
        ch = list.find_all('ul')
    # print(list.img['src'])
        print(ch)
        # data.append({'title': title, 'thumb': thumb, 'ch': ch})

    # for l in list.find('li'):

    return data
