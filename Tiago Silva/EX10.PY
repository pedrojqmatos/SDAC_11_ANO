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
print (counts)
largest = -1
bigcount = None 
for word, count in counts.items() : 
    print( word , count)
    if largest > count :
        count = largest
        bigcount = word 
print ( 'The most common word is:', bigcount, 'with', largest, 'counts')


    

