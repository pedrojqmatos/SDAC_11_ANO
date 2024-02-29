#variável para o ficheiro
fopen = open('mbox-short.txt')

for line in fopen :
    #rstrip = tira espaços
    line = line.rstrip()
   
    #divide a linha em palavras
    words = line.split() 
    if len(words) < 1 or words [0] != 'From' :
        continue
    print(words[2])