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
    dlh = (time.mktime(dl.timetuple()))/3600    #deadline tunneissa
    diff = dlh-h    #ero deadlinen ja nykyheken välillä
    return ("Deadline: " + dl.ctime(),"Tunnit: %.1f" %(diff))
    
