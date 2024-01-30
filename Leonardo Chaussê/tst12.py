fhand = open("mbox-short.txt")

for line in fhand :
    #retira todos os espaços a direita
    line = line.rstrip()
    if not line.startswith('From') :
        continue
    words = line.split
    print (rline.upper())