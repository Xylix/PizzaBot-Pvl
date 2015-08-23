import sqlite3
import json
sqlite_file = 'pizzat.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def printTable(table):
    return c.execute("SELECT * FROM "+table+";")
