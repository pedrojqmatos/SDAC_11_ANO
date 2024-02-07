file = input('enter file:')
if len(file) < 1:
    file = 'clown.txt'
fopen = open(file)
#abrir ficheiro

counts = dict()
for line in fopen:
    words = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 )+1
print(counts)
#decobrir qual é a que contém maior quantidade em dicionario

bigvalue = None
bigkey = None
for key, value in counts.items():
    print(key, value)
    if bigvalue is None or value > bigvalue:
        bigkey = key
        bigvalue = value
print('The most common word is:', bigkey, 'with', bigvalue, 'counts')