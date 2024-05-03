import sqlite3
con = sqlite3.connect("tutorial.db") #para criar a tabela
cur = con.cursor()  #com a variável adiciona o cursor
cur.execute("DROP TABLE movie")
cur.execute("CREATE TABLE movie(title, year, score)")  #vamos iniciar a variaver com o cursor
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
"""
)
con.commit() #vais cometer isto para la

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

cur.executemany("INSERT INTO movie VALUES (?, ?, ?)", data) #vais inserir os valores de acordo com a data
con.commit() #manda e encerra o processo

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

con.close()

new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')



