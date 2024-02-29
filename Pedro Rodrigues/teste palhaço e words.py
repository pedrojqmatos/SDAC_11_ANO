fname = input('Enter file:')
handle = open(fname, enconding = 'utf-8')
#cria dicionário com todos os termos e contagem
counts = dict() #cria dicionário
for line in handle : #veririfica as linas
    words = line.split() #separa a linha em palavras
    for word in words: #itera em cada palavra
        counts[word] = counts.get(word, 0) + 1 #conta a palvra em si, baseada em valor 0 e incrementa + 1 se encontrar a mesma palavra
print(counts) 

#verifica qual o termo mais comum e o seu número correspondente
bigcount = None #define a "nada" o número que a palavra mais comum apareceu
bigword = None #define a "nada" a palavra mais comum

for word, count in counts.items(): #itera nos valores chave(key) e valor(value) dentro dos itens do dicionário criado
    if bigcount is None or count > bigcount: #verifica a condição para quando o valor for maior que None é encontrado = 1 > 0
        bigword = word #identifica a palavra mais comum
        bigcount = count #identifica o número mais repetido da palavra
print(bigword, bigcount)