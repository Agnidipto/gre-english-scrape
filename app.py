import requests
from bs4 import BeautifulSoup
import json

result=[]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", 
"Accept-Encoding":"gzip, deflate", 
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"DNT":"1","Connection":"close", 
"Upgrade-Insecure-Requests":"1"}


index = open('input.json', 'r')
input=json.load(index)

for x in input: 
    source=requests.get('https://dictionary.cambridge.org/dictionary/english/'+x['word'], headers=headers)
    soup=BeautifulSoup(source.text,'lxml')

    entries=soup.findAll('div', class_='examp')
    r=[]
    for i in entries:
        print(i.text.strip())
        r.append(i.text.strip())
    
    res = {
            'word': x['word'],
            'meaning' : x['meaning'],
            'examples': r
        }
    result.append(res)

file = open('output.json','w', encoding="utf-8")
jsoned=json.dumps(result, indent=4, ensure_ascii=False)
file.write(jsoned)
file.close()