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
    h=(time.mktime(t.timetuple()))/3600
    dlh = (time.mktime(dl.timetuple()))/3600  #deadline tunneissa
    diff = dlh-h #ero deadlinen ja nykyheken välillä
    return ("Deadline: " + dl.ctime(),"Tunnit: %.1f" %(diff))

#dl=setDeadLine("2015-08-22 23:50:00")  #pistä sinne komennonlukujuttuun et se antaa tälle sen msgn ja sit et se ottaa takas ton dl
#diff=deadLine(dl)  #ja sit antaa sen sit tuolle deadlinelle ku kysytään



#now = datetime.datetime.fromtimestamp(EpochSeconds)
#or use datetime.datetime.utcfromtimestamp()
#print now
#=> datetime.datetime(2003, 8, 6, 20, 43, 20)
#print now.ctime()
#=> Wed Aug  6 20:43:20 2003

#dl=setDeadLine("2015-08-25 20:00:00")
#deadLine(dl)  #ja sit antaa sen sit tuolle deadlinelle ku kysytään
