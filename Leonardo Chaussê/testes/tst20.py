import urllib.request, urllib.parse, urllib.error

hinput= input("esnter url")

html = urllib.request.urlopen(hinput)


soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))