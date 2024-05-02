import sqlite3
conect = sqlite3.connect("Desafio1.db")
cur = conect.cursor()

cur.execute('DROP TABLE count')

cur.execute('CREATE TABLE count(email TEXT,counts INTEGER)')

oarchive= input("qual arquivo queres abrir?: ")
if (len(oarchive) < 1 ) : oarchive = 'mbox-short.txt'
fh = open(oarchive)

try:
    open(oarchive)
except:
    print("Arquivo não encontrado:",oarchive)
    

