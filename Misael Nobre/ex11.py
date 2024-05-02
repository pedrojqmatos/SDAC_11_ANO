fname = input("Enter the file name : ")
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

new_dict = dict()
for line in handle : 
    line = line.rstrip()
    words = line.split()
    for word in words :
        new_dict[word] = new_dict.get(word, 0) + 1
        
newtup = list()
for v, k in new_dict.items():
    newtup.append((v, k))
    
newtup = sorted(newtup, reverse=True)
for v, k in newtup[:5]:
    print (v, k)