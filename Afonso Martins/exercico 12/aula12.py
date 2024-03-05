fname = input("Enter file: ")
if len(fname) < 1:
    fname = 'clown.txt'
handle = open(fname)

new_dictionary = dict()
for line in handle:
    line.rstrip()
    words = line.split()
    for word in words:
        new_dictionary[word] = new_dictionary.get(word, 0) + 1
        
print(new_dictionary)

largest = -1
tag = None 
for key, value in new_dictionary.items():
    print(key, value)
    if value > largest:
        largest = value
        tag = key
print("The most common word is: ", tag, "with", largest, "countss")
