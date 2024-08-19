import requests 
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/sustainability/cp-scott-centenary-essay"
page = requests.get(url) 

soup = BeautifulSoup(page.content, 'html.parser')


article = soup.find("div",class_="article-body-commercial-selector")

my_string= article.get_text()
words=my_string.split()
print(f"my string is {my_string}")
print(f"the list of words is {words}")
word_count=len(words)
print(f"the number of words is {word_count}")

