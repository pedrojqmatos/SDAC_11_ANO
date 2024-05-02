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
print(new_dictionary)

#verifica qula o termo mais comum e seu numero correspondente
largest = -1
tag= None
for key, value in new_dictionary.items():
    print(key,value)
    if value > largest :
        largest = value   #identifica a palavra mais comum
        tag = key #identifica o maior umero da palavra
print("the most common word is:","'",tag,"'","whith",value,"new_dictionary")