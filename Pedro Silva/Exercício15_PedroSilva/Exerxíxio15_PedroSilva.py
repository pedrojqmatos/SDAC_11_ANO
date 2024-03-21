import sqlite3

con = sqlite3.connect('Exercício15_PedroSilva.sqlite') #connect te file with the DB
cur = con.cursor() 
cur.execute('DROP TABLE IF EXISTS Counts') #drop table if exists the table
cur.execute('CREATE TABLE Counts(email TEXT, count INTEGER)') #create table with email type text and count typr integer


fput = input('Select the file>>> ')
fopen = open(fput)

for line in fopen:
    if not line.startswith('From'): continue
    words = line.split()
    email = words[1]
    cur.execute("SELECT count FROM Counts WHERE email = ?", (email,)) #going select count from Counts and add in table with query = ?
    row = cur.fetchone() #find email in the file.txt 
    if row is None: 
        cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email,))
    else:
        cur.execute("UPDATE Counts SET count = count+1 WHERE email = ?",  (email,))

#if not has insert email = ? and count = 1 else update 
    con.commit()

strsql = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"
for row in cur.execute(strsql): 
    print(str(row[0]), row[1])

con.close()
