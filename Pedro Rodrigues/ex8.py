fname = input("Open the designated file: ")
try :
    fhand = open(fname.upper)
except :
    print("Invalid file ", fname, "name cannot be opened")
    quit()
print(fhand)

for line in fhand:
    lrs = line.rstrip()
    print(lrs.upper)
