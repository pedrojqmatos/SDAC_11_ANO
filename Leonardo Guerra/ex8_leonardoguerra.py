fname = input("Open the designated file : ")
try :
    fhand = open(fname)
    quit()
except :
    print("Invalid file name", fname,"cannot be opened")
    
for file in fhand:
    file = file.rstrip()
    file = file.upper()
    print(file)