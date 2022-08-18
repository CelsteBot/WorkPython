import os
import json
import sys
from requests_html import HTMLSession

session = HTMLSession()

url = "https://web.sachamber.org"
r = session.get(url + "/search")
links = r.html.links
links_list = list(links)
links_list.sort()

final = []

for link in links_list:
    if link[0] != '/':
        continue
    
    detail_page = session.get(url + link)

    a_list = detail_page.html.find('a')
    names = detail_page.html.find('span[itemprop="name"]')

    i = 0
    for a in a_list:
        if a.text == 'Visit Site':
            name = names[i].text
            link = a.links.pop()

            print(names[i].text)
            print(link)
            print()
            i += 1

            final.append({'name': name, 'link': link})
    
    print()

file = open("C:\\Users\\alexa\\Desktop\\PythonProjects\\WebScraper\\data.json", 'w')
json.dump({'list': final}, file, indent=3)
file.close()
