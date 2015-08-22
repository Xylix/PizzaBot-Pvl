import sqlite3
import json
sqlite_file = 'pizzat.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def printTable(table):
    separator = " , "
    ret = ""
    for row in c.execute("SELECT * FROM "+table+";"):
        ret += separator.join(row) + "\n"
        return row

    #return j
    #j=(c.fetchall()).split(")")

    #return str(json.dumps((c.fetchall()), sort_keys=True, indent=4))
    #j = json.loads('{"c.fetchall()" : "3"}')
    #return j['two']
