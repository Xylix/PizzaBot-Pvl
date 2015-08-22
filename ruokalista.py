import sqlite3
sqlite_file = 'pizzat.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def printTable(table):
    c.execute("SELECT * FROM "+table+";")
    return(c.fetchall())
