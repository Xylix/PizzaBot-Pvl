import sqlite3
import json
sqlite_file = 'pizzat.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def printTable(table):
    query = "SELECT * FROM "+table+";"
    print (repr(query))
    return [q for q in c.execute(query)]
