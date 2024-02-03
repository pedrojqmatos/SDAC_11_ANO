file = input('enter file:')

try:
    fopen = open(file)
except:
    fopen = open('clown.txt')
counts = dict()
for line in fopen:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 )+1
print(counts)