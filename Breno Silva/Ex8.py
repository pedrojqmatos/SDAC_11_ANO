fname = input ("Enter the patch file: ")
try: 
    file= open(fname, "r")
except:
    print("File not found or can not be open")
    quit()
for x in file:
    l = x.rstrip()
    print(l.upper())
    
    
