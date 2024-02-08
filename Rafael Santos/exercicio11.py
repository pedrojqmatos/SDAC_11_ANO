file = input('Enter file:')
if len(file) < 1:
    file = 'clown.txt'
fopen = open(file)

counts = dict()
for line in fopen:
    words = line.rstrip
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1


tup =  counts.items()
list = list()
for key, value in tup:
    list.append((value, key))

slist = (sorted(list, reverse = True))[:5]
for k, v in  slist:
    print(k, v)