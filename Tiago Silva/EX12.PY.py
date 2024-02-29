import urllib.request , urllib.parse , urllib.error
inp= input("Open the designated website:")
fhand = urllib.request.urlopen (inp)
counts = {}
for line in fhand :
    words = line.decode().split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1


lst = []
for k, v in counts.items () :
    newtup = (v , k)
    lst.append (newtup)

lst = sorted (lst, reverse = True)
for v, k in lst [ : 10 ]:
    print (k , v )