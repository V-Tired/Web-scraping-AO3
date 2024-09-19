from bs4 import BeautifulSoup
import requests
from pathlib import Path


fic_titles = []
split = []
author_split = []
actual_titles = []
actual_authors = []
url = URL_FROM_AO3


def get_titles():
    only_titles = [i for i in fic_titles if "works" in i and "tags" not in i]
    for each in only_titles:
        new_items = each.split(":")
        split.append(new_items)
    for each in split:
        each[0] = ""
    for each in split:
        item1 = "".join(each)
        actual_titles.append(item1)
    return actual_titles


def get_authors():
    only_authors = [i for i in fic_titles if "users" in i]
    for each in only_authors:
        new_items = each.split(":")
        author_split.append(new_items)
    for each in author_split:
        each[0] = ""
    for each in author_split:
        item1 = "".join(each)
        actual_authors.append(item1)
    return actual_authors


response = requests.get(url)
web = response.text
soup = BeautifulSoup(web, features="html.parser")

titles = soup.select(".work .header .heading a")
for title in titles:
    info = title.getText()
    href = title.get("href")

    item = f"{href}:{info}"
    fic_titles.append(item)

actual_titles = get_titles()
actual_authors = get_authors()
try:
    with open("titles.csv", mode="a") as file:
        file.write("title, author\n")
        for num in range(len(actual_titles)):
            file.writelines(f" {actual_titles[num]},  {actual_authors[num]}\n")
except FileNotFoundError:
    if not Path("titles.csv").exists():
        open(file="titles.csv", mode="w")
        file.write("title, author\n")
        for num in range(len(actual_titles)):
            file.writelines(f" {actual_titles[num]},  {actual_authors[num]}\n")