inp=input("open the designated file: ")
try:
    finp= open(inp)
except:
    print("inavalid file name",inp,"cannot be opened")
    quit()
for line in finp:
    llrs=line.strip()
    print(line.upper())