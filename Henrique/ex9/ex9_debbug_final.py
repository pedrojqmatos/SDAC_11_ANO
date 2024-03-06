fopen = open('mbox-short.txt')

for line in fopen :
    line = line.rstrip()
    words = line.split()
    #guardian robust pattern in a compound statement
    if len(words) < 3  or words[0] != 'From' :
        continue
    print(words[2])