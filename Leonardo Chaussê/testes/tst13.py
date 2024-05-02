counts = dict()
line = input("enter line: ")
words = line.lower()
words = words.split()
print(words)
for word in words :
    counts[word] = counts.get(word, 0) + 1
print ("Counts", counts)