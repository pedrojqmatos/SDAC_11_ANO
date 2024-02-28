name = input("Open the designated file:")
try :
    fhand = open(name)
except:
    print("Invalid file", name , "name cannot be opened")
    quit()
for line in fhand:
  sline = line.rstrip()
print (sline.upper())
