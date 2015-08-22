#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import time
#import komennonluku
#import sendRaw
#import ruokalista

NICK = "pizzaBoy"
CHANNEL = "#botwars"
REALNAME = "Egen ja XyliXin pizzabotti"
pizzaList = []
#velkaList = []
komennot = ["tilaa[tilaaja//pizza//hinta(euroissa, ei euro-merkkiä!)]", "apu", "showlist"]
def command(msg):
    msg = msg[7: ]
    if msg.startswith("tilaa"):
        #print (msg)
        tilaa(msg)
    elif msg.startswith("help"):
        apu()
    elif msg.startswith("deadline"):
        deadline(msg)
    elif msg.startswith("showlist"):
        showList()
def addOrder(user, pizza, order):
    paid = False
    pizzaList.append((user, pizza, order, paid))
def makeString():
    parsed = ""
    print("testiStart")
    for x in range(0, len(pizzaList)):
        print("testiLoop")
        parsed += pizzaList[x][0] + "\n"# + pizzaList[x][1]+ "\n" + pizzaList[x][2]+ "\n"
    return parsed

    #return (pizzaList)

def tilaa(tilaus):
        tilaus = tilaus[5: ]
        tilaus = tilaus.split("//")
        print (tilaus)
        addOrder (tilaus[0], tilaus[1], tilaus[2])

def apu():
    #print ("komennon alkuun !pizza-")
    #print (komennot)
    sendmsg("komennon alkuun!pizza-", CHANNEL)
    sendmsg(komennot, CHANNEL)

def addOrder(user, pizza, order):
    paid = False
    pizzaList.append(    (user, pizza, order, paid)    )
def sendmsg(msg, channel):
    sendRaw("%s %s :%s" % ("PRIVMSG", channel, msg))
def showList():
    sendmsg(makeString(), CHANNEL)

def botti(chan, nick, msg):
    if msg.lower().startswith("!pizza-"):
        command(msg.lower())
    #elif msg.startswith(NICK):
     #   sendmsg("Hiljaa! Baka!!")


# Älä koske tämän alla olevaan koodiin
def sendmsg(msg, channel):
    sendRaw("%s %s :%s" % ("PRIVMSG", channel, msg))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def sendRaw(msg):
    totalsent = 0
    ba = (msg+"\r\n").encode('UTF-8')
    while totalsent < len(ba):
        sent = s.send(ba[totalsent:])
        if sent == 0:
            raise RuntimeError("connection lost")
        totalsent += sent
    print("--> "+msg)


def listenToServer(callback):
    joined = False
    data = []
    while True:
        chunk = s.recv(1024)
        if chunk == '':
            raise RuntimeError("connection lost")
        data.append(chunk)
        lines = b''.join(data).decode("UTF-8").split("\r\n")
        if data[-2:-1] != "\r\n":
            data = [lines[-1].encode("UTF-8")]
            lines = lines[:-1]
        else:
            data = []
        for l in lines:
            print("<-- "+l)
            if l.startswith("PING"):
                sendRaw("PONG :" + l[6:])
            if not joined and l.split()[1] == "001":
                sendRaw("JOIN %s" % CHANNEL)
                joined = True
            else:
                components = l.split()
                if components[1] == "PRIVMSG":
                    nick = components[0][1:].split("!")[0]
                    chan = components[2]
                    msg = " ".join(components[3:])
                    msg = msg[1:]
                    callback(chan, nick, msg)

if __name__ == "__main__":
    try:
        s.connect(("irc.paivola.fi", 6667))
        sendRaw("NICK %s" % NICK)
        sendRaw("USER %s 0 * :%s" % (NICK, REALNAME))
        listenToServer(botti)

    except (KeyboardInterrupt):
        sendRaw("QUIT :Python bot out")
        s.close()
        #raise