import random
import urllib.request
from bs4 import BeautifulSoup

with open('bwv.txt') as f:
	bwv = f.readlines()

n = random.randint(1, 1129)

print("Today's Bach is: \n ", bwv[n])

textToSearch = bwv[n]
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

def printLinks():
	linkList = []
	for i in range(5):
		for vid in soup.find_all(attrs={'class':'yt-uix-tile-link'}):
			v = 'https://www.youtube.com' + vid['href']
			linkList.append(v)
		print(linkList[i])

printLinks()