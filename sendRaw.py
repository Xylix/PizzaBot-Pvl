def sendRaw(msg):
    totalsent = 0
    ba = (msg+"\r\n").encode('UTF-8')
    while totalsent < len(ba):
        sent = s.send(ba[totalsent:])
        if sent == 0:
            raise RuntimeError("connection lost")
        totalsent += sent
    print("--> "+msg)
