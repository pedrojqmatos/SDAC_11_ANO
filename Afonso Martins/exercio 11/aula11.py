fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt"
handle =open (fname)

new_dixtionary =dict()
for line in handle :
    line =line.rstrip()
    words=line.split()
    for word in word :
        new_dictionary(word) = new_dictionary.get(word,0)+1 