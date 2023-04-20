import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.amazon.com/s?i=grocery&rh=n%3A16310101&fs=true&pg=4&qid=1681953982&ref=sr_pg_2")
soup = BeautifulSoup(page.content, 'html.parser')

body = soup.body.text
print(body)