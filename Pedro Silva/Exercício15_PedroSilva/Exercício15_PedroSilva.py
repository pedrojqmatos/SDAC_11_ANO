import sqlite3

con = sqlite3.connect('Exercício15_PedroSilva.sqlite') #connect te file with the DB
cur = con.cursor() 
cur.execute('DROP TABLE counts')
cur.execute('CREATE TABLE counts(count, email)')
