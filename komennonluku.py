komennot = ["tilaa", "apu"]
def komento(msg):
    msg = msg[7: ]
    if msg.startswith("tilaa"):
        print (msg)
        tilaa(msg)
    elif msg.startswith("help"):
        apu()


def tilaa(tilaus):
        tilaus = tilaus[5: ]
        tilaus = tilaus.split("//")
        print (tilaus)

def apu():
    print ("komennon alkuun !pizza-")
    print (komennot)

 

komento("!pizza-tilaa Ege//pizzaa//8.50")

komento("!pizza-help")
