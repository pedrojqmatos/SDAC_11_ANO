fname = input("Enter file: ")
handle = open( fname, encoding = "utf-8")

counts = dict()#cria um dicionario
for line in handle : #verifica as linhas
    words = line.split() #separa as linhas em palavras
    for word in words :#itera em cada palvra
        counts [word] = counts.get(word, 0) + 1
print(counts)

#verifica qula o termo mais comum e seu numero correspondente
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount :
        bigword = word   #identifica a palavra mais comum
        bigcount = count #identifica o maior umero da palavra
print("the most common word is:","'",bigword,"'","whith",bigcount,"counts")