fname = input("Enter files:")
if len(fname) < 1 :
    fname = 'clown.txt'
    handle = open(fname)

counts = dict() 
for line in handle : 
    line.rstrip() 
    words = line.split()
    for word in words : 
        counts[word] = counts.get(word , 0) + 1 

temp = list()
for k, v in counts.items() :
    temp.append((v, k))

temp = sorted(temp , reverse = True)

for v,k in temp [ : 5 ] :
    print (v, k)




