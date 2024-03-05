fname = input("Enter file: ")
if len(fname) < 1:
    fname = "clown.txt"
text = open(fname)

counts = dict()
for line in text:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print (counts)

for (k,v) in counts.items():
    print (k,v)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count
print("The most common word is:", bigword, "with", bigcount,"counts")

