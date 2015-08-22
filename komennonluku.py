#!/usr/bin/python
# -*- coding: utf-8 -*-
pizzaList = []
velkaList = []
komennot = ["tilaa[tilaaja//pizza//hinta(euroissa, ei euro-merkkiä!)]", "apu"]
def command(msg):
    msg = msg[7: ]
    if msg.startswith("tilaa"):
        print (msg)
        tilaa (msg)
    elif msg.startswith("help"):
        apu()
    elif msg.startswith("deadline"):
        deadline()
def addOrder (user, pizza, order):
    paid = False
    pizzaList.append(    (user, pizza, order, paid)    )

def tilaa(tilaus):
        tilaus = tilaus[5: ]
        tilaus = tilaus.split("//")
        print (tilaus)
        addOrder (tilaus[0], tilaus[1], tilaus[2])

def apu():
    print ("komennon alkuun !pizza-")
    print (komennot)
def addOrder (user, pizza, order):
    paid = False
    pizzaList.append(    (user, pizza, order, paid)    )

#testit
#command("!pizza-tilaa Ege//pizzaa//8.50")
#command("!pizza-help")
#addOrder ("xylix", "al-capone", 12)
#addOrder ("Ege", "tropicana", 12)
