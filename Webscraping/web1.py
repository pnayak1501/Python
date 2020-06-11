import requests
import bs4

res=requests.get('http://instagram.com')
soup=bs4.BeautifulSoup(res.text,'lxml')
hi=soup.select('title')               #here hi is iteratable
print(hi)
print(hi[0].getText())