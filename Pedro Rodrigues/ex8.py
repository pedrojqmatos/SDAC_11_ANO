#ex8

fname = input("Open the designated file: ")
try :
    fhand = open(fname)
except :
    print("Invalid file name", fname, "cannot be opened")
    quit()

for line in fhand:
    lrs = line.rstrip()
    print(lrs.upper())