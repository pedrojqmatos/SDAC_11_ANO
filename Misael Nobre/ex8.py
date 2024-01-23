fname = input("Open the designated file : ")
try :
    fhand = open(fname)
except :
    print("Invalid file name", fname,"cannot be opened")
    quit()
    
for file in fhand:
    file = file.rstrip()
    file = file.upper()
    print(file)