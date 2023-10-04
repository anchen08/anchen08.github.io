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

file = open("completed.txt", "r")
cities = file.readlines()
file.close()
# cities = ["Altoona"]

file = open("new_cleaned_short.txt", 'r')
temp = file.readlines()
search_terms = list(map(lambda x: x.rstrip('. \n'), temp))
file.close()

# file = open("new_cleaned.txt", 'r')
file = open("new.txt", 'r')
temp = file.readlines()
write_terms = list(map(lambda x: x.rstrip('. \n'), temp))
file.close()

stripped = list(map(lambda x: x.rstrip('\n').lower(), cities))
url_cities = list(map(lambda x: x.replace(' ', ''), stripped))

error_log = open("errorlog_scanning.txt", 'w')

for i, city in enumerate(cities):
    current_city = open("city_info/" + url_cities[i] + ".html", "w")

    url_city = url_cities[i]
    full_url = url + url_city
    response = requests.get(full_url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    soup_str = str(soup)

    for i, category in enumerate(search_terms):
        index = soup_str.find(category)

        if index == -1: # not found
            current_city.write(f"<strong>{write_terms[i]}</strong>")
            current_city.write("<br>")
            current_city.write(f"n/a")
            current_city.write("<br><br>")
            pass
        else: 
            index += len(category) -1 # skip over the starting
            index = soup_str.find('</strong></p><p>',index)
            end_index = soup_str.find('<p><strong>', index)


            if (end_index == -1):
                end_index = soup_str.find("Photo Gallery", index)
            if (end_index == -1):
                end_index = soup_str.find("About Our Community", index)

            current_city.write(f"<strong>{write_terms[i]}</strong>")
            current_city.write(soup_str[index:end_index])
            current_city.write("<br><br>")

    current_city.close()


error_log.close()
