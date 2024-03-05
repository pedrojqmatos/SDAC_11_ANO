finput = input ("Open the designated file:")
#testes for file validity
try:
    fhand = open(finput)
except:
    print ("Invalid file name", finput , "cannot be opened")
    quit()
#executes the file reading removes right space for new line and converts in
    for line in fhand:
        lrs = line.rstrip()
        print(lrs.upper())
        