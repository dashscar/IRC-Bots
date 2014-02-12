import sys
import socket
import string
import time
import subprocess
HOST="server"
PORT=6667
NICK="eval"
IDENT="eval"
REALNAME="eval"
CHAN="#channel"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
time.sleep(3)
s.send("JOIN :%s\r\n" % CHAN)
#s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Hello there, I am Quote Bot"))
#s.send("PRIVMSG %s :%s\r\n" % (CHAN, 'Just type ".quote" for some historical wisdom!'))

nodont = "5SECURITY BLOCK: 4UNAUTHORIZED COMMAND ATTEMPTED!"

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        print line[3:]
        if(":.eval" in line):
            reply = ""
            privnick = 0
            if line[2][0] == "#":
                target = CHAN
            else:
                splstr = line[0].split('!', 1)
                privnick = splstr[0][1:]
                target = privnick
            if target == privnick:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
            if "alias" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "chown" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "while" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "/dev/urandom" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "perl" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "kill" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "cmatrix" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "nano" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "vim" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "vi" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
#            if "cat" in line:
#                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
#                line = [[""]*10]
            if "killall" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "eval.py" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "-9" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "yes" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "of=/dev/sda" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "-rf" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10] 
            if ":(){" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "*" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
                line = [[""]*10]
            if "su" in line:
                s.send("PRIVMSG %s :%s\r\n" % (target, nodont))
            p = subprocess.Popen(" ".join(line[4:]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line2 in p.stdout.readlines():
                reply = line2
                s.send("PRIVMSG %s :%s\r\n" % (target, reply))
#            print line[2][0]
        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])
