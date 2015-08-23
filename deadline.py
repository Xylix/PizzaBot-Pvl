#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime

def setDeadLine(msg):
    msg=msg[12: ]
    dl = datetime.datetime.strptime(msg, "%Y-%m-%d %H:%M:%S")
    return dl
def deadLine(dl):
    t = datetime.datetime.now() #aika nyt
    #print (t)
    #dl = datetime.datetime(2015, 8, 23, 15, 00, 00)   #deadLine
    h=(time.mktime(t.timetuple()))/3600
    dlh = (time.mktime(dl.timetuple()))/3600  #deadline tunneissa
    diff = dlh-h #ero deadlinen ja nykyheken välillä
    #sendmsg("Tunnit: %.1f" %(diff))
    #sendmsg("Deadline: " + dl.ctime())
    return ("Deadline: " + dl.ctime(),"Tunnit: %.1f" %(diff))

#dl=setDeadLine("2015-08-25 20:00:00")
#deadLine(dl)  #ja sit antaa sen sit tuolle deadlinelle ku kysytään
