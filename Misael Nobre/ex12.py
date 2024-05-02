import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url : ')
html = urllib.request.urlopen(url)
count = dict()
for line in html:
    words = line.decode().split()
    for word in words: count[word] = count.get(word, 0) + 1
lst = []
for key, val in count.items(): newtop = (val, key) ; lst.append(newtop)
lst = sorted(lst,reverse=True)
for val, key in lst[:10]: print(key, val)