fname = input('Enter file: ')
if len(fname) < 1:              #para perceber se a algo no input 
    fname = 'clown.txt'
handle = open(fname)

new_dicionary = dict()
for line in handle :
    line.rstrip()
    words = line.split()
    for word in words :
        #idiom: retrieve/create/update counter
        new_dicionary[word] = new_dicionary.get(word, 0) + 1

print(new_dicionary)

#encontra a palavra mais comum
largest = -1
tag = None
for key, value in new_dicionary.items() :
    print(key, value)
    if value > largest :
        largest = value
        tag = key #irá caputrar a palavra mais comum
print("The most common word is: ", tag, 'with',largest, 'counts')
    

