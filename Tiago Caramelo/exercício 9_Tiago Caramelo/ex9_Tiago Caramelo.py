#variável para o ficheiro
fopen = open('mbox-short.txt')

for line in fopen :
    #rstrip = tira espaços
    line = line.rstrip()
    print('This is line: ', line)      #testar se a linha do "line" está correta
    #divide a linha em palavras
    words = line.split() 
    print('This is words: ', words)    #testar se a linha do "words" está correta
    # Guardian pattern
    if len(words) < 1 :   #se o len daquela linha for menor que (1), continua  
        continue
    # (!=) = diferente
    if words[0] != 'From' :
        print('Ignored')       #na posição (0) e for diferente de 'From' ele irá ignorar  
        continue
    #vai dar erro pois como a lista vai ficar vazia nao vai ter nada no espaço (2)
    print(words[2])      


