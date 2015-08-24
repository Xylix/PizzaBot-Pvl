import sqlite3
#import json
sqlite_file = 'pizzat.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def printTable(table):
    table = table[0:6]
    return c.execute("SELECT * FROM "+table+";")
#    separator = ", "
    ret = ""
    for row in c.execute("SELECT * FROM "+table+";"):
        ret += separator.join(str(i) for i in row) + "\n"
    return ret


    # query = "SELECT * FROM "+table+";"
    # print (repr(query))
    # return [q for q in c.execute(query)]
