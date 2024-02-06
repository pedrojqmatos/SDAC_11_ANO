fopen = open('mbox-short.txt')

for line in fopen :
    line = line.rstrip()
    words = line.split()
    print('Words', words)
    if words[0] != 'From' :
        continue
    print(words[2])