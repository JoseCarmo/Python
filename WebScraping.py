
''' Use the BeautifulSoup and requests Python packages to print out 
a list of all the article titles on the New York Times homepage. '''

from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('nyt_titles.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['text'])

url = 'https://www.nytimes.com/'
request_page = requests.get(url).text
soup = BeautifulSoup(request_page, 'html.parser')

for article in soup.find_all(class_= 'story-heading'):

    print((article.text.replace("\n", " ").strip()) + '\n')
    csv_writer.writerow([article.text.replace("\n", " ").strip()])

csv_file.close()