import requests
from bs4 import BeautifulSoup
import os

search = input('type something to search in wiki: ')

url = "https://en.wikipedia.org/wiki/"+search
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

result_list = soup.findAll('div')
for div in result_list:
    R1=div.find('h1')
    if(R1!=None):
        print(R1.string)
        print("\n")
print("Printing inner first table:")
bodyResult = soup.find('body')
for table in bodyResult:
    R2=table.find('table')
    if(R2!=None and R2!=-1):
        print(R2)
        break