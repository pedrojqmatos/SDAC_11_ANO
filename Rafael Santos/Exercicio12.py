import urllib.request, urllib.parse, urllib.error

url = input("Enter url:")
furl = urllib.request.urlopen(url)

counts = dict()
for line in furl:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word , 0) + 1

tup =  counts.items()
list = list()
for k, v in tup:
    list.append((v, k))

slist = (sorted(list, reverse = True))[:10]
for v, k in  slist:
    print(k, v)





