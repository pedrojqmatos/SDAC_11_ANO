fopen = open('test10.txt')
print(fopen)
for line in fopen:
    line = line.rstrip()
    words = line.split()
    print("words is -- ", words)
    if line == '':
        print("skip blank line")
    if len(words) < 1 :
        continue
    if words[0] != 'From' :
        print("Ignored --")
        continue
    print(words[2])
   
   # guardian robust pattern in a compound statement  
  #  if len(words) < 1 or words[0] != 'From':