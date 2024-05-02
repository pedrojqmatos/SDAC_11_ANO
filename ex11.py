file = input('enter file:')
if len(file) < 1: file = 'clown.txt'
try: fopen = open(file)
except: print('Identifica a extesão do ficherio') , exit()

counts = dict()
for line in fopen:
    words = line.rstrip()
    words = line.split()
    for word in words: counts[word] = counts.get(word, 0 )+1

lista = list()
for key, value in counts.items(): lista.append((key, value))
lista = sorted(lista, reverse=True)

for key, value in lista[:5]: print(key, value)