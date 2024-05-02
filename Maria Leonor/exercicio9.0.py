fopen = open ("mbox-short.txt")

for line in fopen :
    line = line.rstrip()
    print("this is line")
    words = line.split()
    print("this is words", words)
if words (0) = "From":
print ("ignored")
continue:
