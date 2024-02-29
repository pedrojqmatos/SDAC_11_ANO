fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

new_dictionary = dict()
for line in handle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        #idiom: retrieve/create/update counter
        new_dictionary[word] = new_dictionary.get(word, 0) + 1
   
temp = list()
for k, v in new_dictionary.items() :
    temp.append(v,k)
    
temp = sorted(temp, reverse=True)

for v,k in temp[:5] :
    print(k,v)