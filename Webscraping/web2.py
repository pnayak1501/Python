import requests
import bs4

res=requests.get('http://instagram.com')
soup=bs4.BeautifulSoup(res.text,'lxml')

for i in soup.select('.mw-headline'):     #or '.toc > ul > li'
    print(i.getText())

