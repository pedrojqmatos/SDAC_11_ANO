counts = dict()
line = input('Enter line')
words = line.split()
print(words)
for word in words :
    counts[word] = counts.get(word, 0) + 1
    print('Counts', words)