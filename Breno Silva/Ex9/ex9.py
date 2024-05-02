fopen = open('mbox-short.txt')

for line in fopen :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3  or words[0] != 'From' :
        continue
    print(words[2])
    