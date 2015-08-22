#!/usr/bin/python
# -*- coding: utf-8 -*-
komennot = ["tilaa[tilaaja//pizza//hinta(euroissa, ei euro-merkkiä!)]", "apu"]
def komennonluku(msg):    
    msg = msg[7: ]
    if msg.startswith("tilaa"):
        print (msg)
        tilaa(msg)
    elif msg.startswith("help"):
        apu()
    elif msg.startswith("deadline"):
        deadline()
        

def tilaa(tilaus):
    tilaus = tilaus[5: ]
    tilaus = tilaus.split("//")
    print (tilaus)

def apu():
    print ("komennon alkuun !pizza-")
    print (komennot)


komennonluku("!pizza-tilaa Ege//pizzaa//8.50")

komennonluku("!pizza-help")
