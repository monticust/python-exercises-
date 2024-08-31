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

set_of_words=set(words) 
word_count2=len(set_of_words)
print(f"no.of unique words {word_count2}")

frequencies = {}


def get_frequency(key,words):
 return sum(1 for i in words if i==key)


for key in set_of_words : 
    f=get_frequency(key,words)
    frequencies[key] = f


  
# def get_frequency(key,words):
#  frequency=0
#   for word in words:
#      if word==key:
#         frequency=frequency+1 
#   return frequency 

print(frequencies)



most_frequent_word=""
highest_frequency=0
for word, frequency in frequencies.items(): 
   if frequency > highest_frequency:
      most_frequent_word=word 
      highest_frequency=frequency 

print(f"the most frequent word is {most_frequent_word}")
print(f"it occurs {highest_frequency} amount of times")

list_of_words=sorted(frequencies.items(), key=lambda x:x[1], reverse= True)
 

print("before")



print("the top ten most frequent words are")

for i in range(10):
 print(list_of_words[i])



print("after")

