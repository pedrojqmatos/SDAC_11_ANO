fopen = open ('mbox-short.txt')

for line in fopen :
    line = line.rstrip()
    print ('Line:', line)
    words = line.split()
    print('Words:', words)
    #Guardian Pattern
    if len(words) < 1 or words[0] != 'From' :
        continue
    if words[0] != 'From' :
       print('Ignored')
       continue
    print(words[2])
