import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://jobs.mo.gov/content/missouri-warn-notices-py-2017")
soup = BeautifulSoup(res.content,'lxml')
# soup = BeautifulSoup(res.content,'html.parser')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))
