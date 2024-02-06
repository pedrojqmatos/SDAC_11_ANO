fname = input("Enter the file name : ")
if len(fname) < 1 :
    fname = 'clown.txt'
handle = open(fname)

new_dict = dict()
for line in handle : 
    line = line.rstrip()
    words = line.split()
    for word in words :
        new_dict[word] = new_dict.get(word, 0) + 1
        
print (new_dict)

largest = -1
capt = None
for key, value in new_dict.items():
    print (key, value)
    if value>largest:largest = value
    capt = key
print("The most common word is:", capt, "with", largest, "count")