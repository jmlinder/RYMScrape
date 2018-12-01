#!/usr/bin/env python
# coding: utf-8

# In[84]:


import requests
from bs4 import BeautifulSoup

url = "https://rateyourmusic.com/new_releases"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
table = soup.find("table", class_="mbgen")

# Finds releases by multiple artists
for multi in table.find_all("span", class_="credited_name"):
    print("Artist:", multi.contents[0])
    print("Album:", multi.findNextSibling("a", class_="album").text)
    print("Release date:", multi.findNextSibling("span", class_="smallgray").text.strip("()").replace("  ", " "))
    print("\n")

# Finds releases by a single artist
for release in table.select("td > a.artist"):
    print("Artist:", release.text)
    print("Album:", release.findNextSibling("a", class_="album").text)
    print("Release date:",release.findNextSibling("span", class_="smallgray").text.strip("()").replace("  ", " "))
    print("\n")


# In[ ]:




