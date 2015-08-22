#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import time
import ruokalista
import json

def getOrders():
    f = open("tilausLista.txt", "r")
    orderList = f.read()
    f.close()
    pizzaList = []
    for i in orderList.split("\n"):
        pizzaList.append(i.split(","))
    print (len(pizzaList), len(pizzaList[0]))
    return pizzaList


NICK = "pizzaBoy"
CHANNEL = "#botwars"
REALNAME = "Egen ja XyliXin pizzabotti"
pizzaList = getOrders()
print(type(pizzaList))
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
    elif msg.startswith("showmenu"): #Muista valita mikä menu listataan (vaihtoehdot [muut, pizzat])
        if " " in msg:
            showMenu(msg.split(" ")[1])
        else:
            sendmsg("Syntaxi komennolle on !pizza-showmenu [muut tai pizzat]")


def addOrders(user, pizza, order):
    paid = False
    pizzaList.append((user, pizza, order, paid))

def makeString(x):
    parsed = pizzaList[x][0] + " // " + pizzaList[x][1] + " // " + pizzaList[x][2] + "€"
    return parsed

    #return (pizzaList)

def tilaa(tilaus):
        tilaus = tilaus[5: ]
        tilaus = tilaus.split("//")
        print (tilaus)
        addOrder (tilaus[0], tilaus[1], tilaus[2])
        addOrders(tilaus[0], tilaus[1], tilaus[2])

def apu():
    #print ("komennon alkuun !pizza-")
    #print (komennot)
    sendmsg("komennon alkuun!pizza-", CHANNEL)
    sendmsg(komennot, CHANNEL)

def addOrder(user, pizza, order):
    paid = False
    global pizzaList
    pizzaList.append((user, pizza, order))
    f = open("tilausLista.txt", "r")
    orderList = f.read()
    orderList += ", ".join((user, pizza, order)) + "\n"
    f.close()
    f = open("tilausLista.txt", "w")
    f.write(orderList)
    f.close()

def sendmsg(msg, channel=CHANNEL):
    sendRaw("%s %s :%s" % ("PRIVMSG", channel, msg))

def showList():
    for x in range(0, len(pizzaList)-1):
        sendmsg(makeString(x), CHANNEL)

def showMenu(table):
    sendmsg(ruokalista.printTable(table))

def botti(chan, nick, msg):
    if msg.lower().startswith("!pizza-"):
        command(msg.lower())
    #elif msg.startswith(NICK):
     #   sendmsg("Hiljaa! Baka!!")

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
