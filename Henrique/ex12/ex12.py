import urllib.request, urllib.parse, urllib.error

hinput = input('Enter url: ')
fhand = urllib.request.urlopen(hinput)

counts = dict()
for line in fhand :
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

temp = list()
for k, v in counts.items() :
    newtup = (v,k)
    temp.append(newtup)
    
temp = sorted(temp, reverse=True)

for v,k in temp[:10] :
    print(k, v)