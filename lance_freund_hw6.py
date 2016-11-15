#!/bin/env python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---

# import urlopen from urllib
from urllib.request import urlopen
import re

def Find(patt, text):
    patt = re.search(parr, text)
    if patt:
        print(patt.group())
    else:
        print('Not Found')

# get a copy of file provided as input $1
with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test") as error_sheet:
    errors=[]
    for err in error_sheet:
        line = err.decode('utf-8')
        line.split()
        for i in line:
                errors.append(line)
                x = str(line.split())
                jabber = x
               # print(type(jabber))
                part = re.search('/..........................', jabber)
                if part:
                    print(part.group())


exit(0)
