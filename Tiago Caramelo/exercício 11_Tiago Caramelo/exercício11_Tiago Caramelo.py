fname = input('Enter file: ')
if len(fname) < 1:              #para perceber se a algo no input 
    fname = 'clown.txt'
handle = open(fname)

new_dicionary = dict()
for line in handle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        #idiom: retrieve/create/update counter
        new_dicionary[word] = new_dicionary.get(word, 0) + 1


temp = list()  #lista vazia
for k, v in new_dicionary.items() :
    temp.append((v,k))


temp = sorted(temp, reverse=True)

for v, k in temp[:5] :  #do inicio até a posição 5
    print(k, v)



