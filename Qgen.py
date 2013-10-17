import sys
import socket
import string
import time
from random import choice
from random import randrange

tenper = randrange(1,11)
fifiy = randrange(1,3)
quote = ''

PreWrittenQuotes = ["One, two, three, four, let me hear you scream if you want some more! Like uhh, push it, push it, watch me work it, I'm perfect!", 
        'Has anyone really been so far as to go look as decided for?',
        'Do you even lift?',
        "They don't think it be like it is, but it do",
        "Deal with it"
        "Give her the dick"]

EvolveVerb = ['evolved', 'come']
Sciencething = ['grains of sand', 'atom', 'brain', 'body', 'star', 'electron', 'molecule', 'software', 'music', 'song', 'program']
Species = ['dog', 'cat', 'whale', 'chicken', 'dolphin', 'human', 'monkey']
EvSpecies = ['human', 'monkey', choice(Species), choice(Species)]
CharactersOnly = ['Spock', 'Harry Potter', 'Neo', 'Luke', 'Gandalf', 'Darth Vader']
Person = [choice(CharactersOnly), 'Carl Sagan', 'Albert Einstein', 'Oprah', 'Steve Jobs', 'Obama', 'Bill Cosby', 'Richard Stallman', 'Linus Torvalds']
Namecall = ['asshole', 'retard', 'faggot']
Adjective = ['fucking', 'stupid', 'annoying', 'retarded']
Entire = ['an entire inch', 'the entire world', 'the entire universe', 'the whole galaxy', 'an entire building', 'a whole continent']
Teleken = ['force', 'death grip', 'mind meld']
EndSentence = ['!', '?', '?!', '.', '!1!1!!!11!!', '!!111!!11!', '???', '!!!']
ListRand = [choice(Sciencething), choice(EvSpecies)]

def pluralize(word):
    if word[-1] == "y":
        if word[-2] in ['a','e','i','o','u']:
            word = word + "s"
        else:
            word = word[:-1] + "ies"
        return word
    else:
        return word + 's'

def quote1():
    #rand1 = randrange (1,11)
    result = 'If ' + pluralize(choice(EvSpecies)) + ' ' + choice(EvolveVerb) + ' from ' + pluralize(choice(EvSpecies))
    result +=' then ' + pluralize(choice(EvSpecies)) + ' must have ' + choice(EvolveVerb) + ' from ' +  pluralize(choice(EvSpecies))
    return result
def quote2():
    #rand1 = randrange(1,11)
    Lrand2 = [choice(Entire), choice(ListRand)]
    morl = ['more ', 'less ']
    result = 'There are ' + choice(morl) + pluralize(choice(Sciencething)) + ' in ' + choice(Lrand2)
    result +=' than there are ' + choice(ListRand) + ' in ' + choice(Lrand2)
    return result
def quote3():
    result = 'Did you know that if you take ' + str(randrange(1,1000)) + ' ' + pluralize(choice(ListRand)) + ", and put them together, they'd fill up all the space in " + choice(Entire) + '?'
    return result
def quote4():
    result = 'Use the ' + choice(Teleken) + ' ' + choice(CharactersOnly) + choice(EndSentence)
    return result
def quote5():
    result = choice(Person) + ' is a ' + choice(Adjective) + ' ' + choice(Adjective) + ' ' + choice(Namecall)
    return result

def genlist():
    ChooseQ = [quote1(), quote2(), quote3(), quote4(), quote5()]
    return ChooseQ
#print pluralize("chicken")
def getquote():
    quote = '"' + choice([choice(PreWrittenQuotes)] + [choice(genlist())] * 10 ) + '" -' + choice(Person)
    return quote
HOST="irc.bagelbox.org"
PORT=6667
NICK="Quotebot"
IDENT="Quotebot"
REALNAME="Quotebot"
CHAN="#bagel"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
time.sleep(3)
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Hello there, I am Quote Bot"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, 'Just type ".quote" for some historical wisdom!'))

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        
        if(":.quote" in line):
            if line[2][0] == "#":
                target = CHAN
            else:
                splstr = line[0].split('!', 1)
                privnick = splstr[0][1:]
                target = privnick
            s.send("PRIVMSG %s :%s\r\n" % (target, getquote()))
            print line[2][0]
        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])
