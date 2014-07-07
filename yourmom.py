import sys
import socket
import string
import time
from random import choice
from random import randrange

#[':SpryX!~Sprylitol@Rizon-895EB333.lightspeed.irvnca.sbcglobal.net', 'PRIVMSG', '#/g/punk', ':this', 'is', 'test']

def yourmom(line):
    x = (line.index("is")) - 1
    line[x] = 'your mom'
    ret = ' '.join(line[3:])
    return ret

HOST="irc.rizon.net"
PORT=6667
NICK="yourmom_bot"
IDENT="Quotebot"
REALNAME="Quotebot"
CHAN="#/g/punk"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
time.sleep(3)
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Hello there, I am Your Mom Bot"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, 'Enjoy :^)'))

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        
        if("is" in line):
            if line[2][0] == "#":
                target = CHAN
            else:
                splstr = line[0].split('!', 1)
                privnick = splstr[0][1:]
                target = privnick
            if randrange(0, 100) < 40:
                s.send("PRIVMSG %s :%s\r\n" % (target, yourmom(line)))
            print line[2][0]
        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])
