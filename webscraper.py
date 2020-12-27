# webscraper-for-amazon-
import requests
from bs4 import BeautifulSoup

print('Enter the URL:')
url = input()
r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
soup = BeautifulSoup(r.text, 'html.parser')
availability = soup.find(id="availability").get_text()
string = str(availability, encoding='utf-8')
print(string)
#

