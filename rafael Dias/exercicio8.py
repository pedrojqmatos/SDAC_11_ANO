finput = input("Open the designated file:")
try :
    fhand = open(finput)
except :
    print('Invalid file name' , finput , 'cannot be opened')
    quit()
for line in fhand :
    lrs = line.rstrip()
    print(lrs.upper())