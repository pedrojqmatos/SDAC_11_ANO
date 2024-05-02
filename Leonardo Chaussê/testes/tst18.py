fname = input("Enter file: ")
#handle = open(fname, encoding = "utf-8") 

if len(fname) < 1:
    fname = "clown.txt" 

handle = open(fname)

new_dictionary = dict()#cria um dicionario
for line in handle : #verifica as linhas
    line.rstrip() #separa as linhas em palavras
    words = line.split()
    for word in words :#itera em cada palvra
        new_dictionary [word] = new_dictionary.get(word, 0) + 1

#verifica qula o termo mais comum e seu numero correspondente
temp = list()
for k, v in new_dictionary.items():
    temp.append((v,k))

temp = sorted(temp, reverse=True)

for v,k in temp[:5]:
    print (v,k)
    