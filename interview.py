#import urllib2 didnt work cause of my python version
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

website = "https://jobs.mo.gov/content/missouri-warn-notices-py-2017"
web_page = urlopen(website)

soup = BeautifulSoup(web_page, 'html.parser')
tables = soup.findAll("table")

finalOutput = []
#holds table column title names
titles = []
for table in tables:
    span = table.findAll('span')
    for tableH in span:
        if tableH:
            titles.append(tableH.text)

#holds data of each cell
detail =[]
data_dictionary = {}
number = 0
for table in tables:
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            number+=1
            text = td.text
            detail.append(text)

"""puts all the data in each row in the list using dictionary format """
k = 0
while k<number:
    for j in range(len(titles)):
            data_dictionary[titles[j]] = detail[k]
            k +=1
    finalOutput.append(data_dictionary)#contains the whole table
    data_dictionary = {}
finalOutput.pop() #removes total column

#print formatting each row on a single line
for i in finalOutput:
    print (i)
    print()
