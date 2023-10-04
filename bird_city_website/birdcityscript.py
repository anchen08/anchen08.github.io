import requests
from bs4 import BeautifulSoup
import os

directory = "results"

if not os.path.exists(directory):
    os.makedirs(directory)

# specify the URL of the web page to scrape
#url = "https://birdcitywisconsin.org/bird-city/" + "madison"
url = "https://birdcitywisconsin.org/bird-city/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

file = open("cities.txt", "r")
cities = file.readlines()
file.close()

# cities = ["eauclaire", "Monroe", "Princeton"]

stripped = list(map(lambda x: x.rstrip('\n').lower(), cities))
url_cities = list(map(lambda x: x.replace(' ', ''), stripped))

error_log = open("errorlog.txt", 'w')
html_page = open("bird_cities.html", "w")

for i, city in enumerate(cities):
    url_city = url_cities[i]

    full_url = url + url_city
    response = requests.get(full_url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    soup_str = str(soup)

    index = soup_str.find("About Our Community")

    index_end = soup_str.find("Community Map")

    if index != -1:
        print(f"{city} is found")
        if (index_end == -1):
            index_end = index + 1500

        html_page.write(f"{city}")
        html_page.write("<br>")
        html_page.write(soup_str[index:index_end])
        html_page.write("<br>\n<br>")
        # html_page.write("\")

    else:
        print(f"{city} not found.")
        error_log.write(f"{city}\n")


error_log.close()
html_page.close()