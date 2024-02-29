fname = input('Enter file: ')
if len(fname) < 1 :
    fname = 'clown.txt'
handle = open(fname)

new_dict = dict()
for line in handle:
    line.rstrip()
    words = line.split()
    for word in words :
        #idiom: retrieve/create/update counter
        new_dict[word] = new_dict.get(word, 0) + 1

print(new_dict)

#finding the most common word
largest = -1
tag = None

for key, value in new_dict.items() :
    print(key, value)
    if value > largest :
        largest = value
        tag = key #capture/remember the largest word
print('The most common word is: ', tag, 'with', largest, 'counts')
