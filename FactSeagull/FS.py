import sys
import socket
import string
import time
from random import choice
from random import randrange

fname = 'Facts.txt'

def fact():
    with open("Facts.txt") as f:
        content = f.readlines()
    return content
def feel():
    with open("Feels") as f:
        content = f.readlines()
    return content
def getquote(qtype):
    if qtype == "fact":
        content = fact()
    if qtype == "feel":
        content = feel()
    quote = choice(content)
    return quote
HOST="irc.bagelbox.org"
PORT=6667
NICK="FactSeagull"
IDENT="FactSeagull"
REALNAME="Fact Seagull"
CHAN="#bagel"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
time.sleep(3)
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Hello there, I am Fact Seagull"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, 'Just type ".fact" for a fact!'))

def checknsend(line, check, message)
    if(check in line):
        if line[2][0] == "#":
            target = CHAN
        else:
            splstr = line[0].split('!', 1)
            privnick = splstr[0][1:]
            target = privnick
        s.send("PRIVMSG %s :%s\r\n" % (target, message))
        print line[2][0]
    if check == ".add":
        with open('Facts.txt', 'a') as file:
            file.write(' '.join(line[4:]))
while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        
        checknsend(line, ":.mean", getquote('feel'))
        checknsend(line, ":.fact", getquote('fact'))
        checknsend(line, ":.add", "Fact added")
        
        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])
