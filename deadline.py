import time
import datetime
import re

def setDeadLine(msg):
    #dl = re.split(r"[,.;:]",msg)
    dl = datetime.datetime.strptime(msg, "%Y-%m-%d %H:%M:%S")
    #print ("dadline: " + str(dl))
    return dl
def deadLine(dl):
    t = datetime.datetime.now() #aika nyt
    #print (t)
    #dl = datetime.datetime(2015, 8, 23, 15, 00, 00)   #deadLine
    h=(time.mktime(t.timetuple()))/3600
    dlh = (time.mktime(dl.timetuple()))/3600  #deadline tunneissa 
    #print (h)
    diff = dlh-h #ero deadlinen ja nykyheken välillä
    print ("Tunnit: %.1f" %(diff))
    print ("Deadline: " + dl.ctime())

dl=setDeadLine("2015-08-25 20:00:00")  #pistä sinne komennonlukujuttuun et se antaa tälle sen msgn ja sit et se ottaa takas ton dl
deadLine(dl)  #ja sit antaa sen sit tuolle deadlinelle ku kysytään


#now = datetime.datetime.fromtimestamp(EpochSeconds)
#or use datetime.datetime.utcfromtimestamp()
#print now
#=> datetime.datetime(2003, 8, 6, 20, 43, 20)
#print now.ctime()
#=> Wed Aug  6 20:43:20 2003

