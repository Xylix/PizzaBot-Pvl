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
    print ("Tunteja deadlineen: %.1f" %(diff))
    print ("Deadline: " + dl.ctime())
    return diff

dl=setDeadLine("2015-08-22 23:50:00")  #pistä sinne komennonlukujuttuun et se antaa tälle sen msgn ja sit et se ottaa takas ton dl
diff=deadLine(dl)  #ja sit antaa sen sit tuolle deadlinelle ku kysytään

if (diff <= 2): 
    if (diff == 2):
        print("2 h deadlineen!")
        #sendmsg("Kaksi tuntia deadlineen!", CHANNEL)
    elif (diff == 1):
        print("1 h deadlineen!")
        #sendmsg("Tunti deadlineen!", CHANNEL)
    elif (diff == 0.5):
        print("30 minuuttia deadlineen!")
        #sendmsg("Puoli tuntia deadlineen!", CHANNEL)
    elif (diff == 0.25):
        print("15 minuuttia deadlineen!")
        #sendmsg("15 minuuttia deadlineen!", CHANNEL)


#now = datetime.datetime.fromtimestamp(EpochSeconds)
#or use datetime.datetime.utcfromtimestamp()
#print now
#=> datetime.datetime(2003, 8, 6, 20, 43, 20)
#print now.ctime()
#=> Wed Aug  6 20:43:20 2003

