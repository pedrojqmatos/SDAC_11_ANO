name = input('enter file:')


if name == ' ':
    fopen = open('clown.txt')
    counts = dict()
    for line in fopen:
        words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 )+1

elif name != ' ':
    fopen = open(name, encoding='utf-8')
    counts = dict()
    for line in fopen:
        words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 )+1
print('The most common word is:', counts)
