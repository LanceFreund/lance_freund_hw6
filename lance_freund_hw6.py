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
    count=0
    for err in error_sheet:
        line = err.decode('utf-8')
        para = re.findall(r"'(.*?)'", str(line))
        para2 = re.findall(r"/(.*?)\s", str(line))
        parastrip = re.findall(r"/icarus(.*?)\s", str(line))
        numms = re.findall(r"\d(.)", str(line))
        for eachP in para2:
            if parastrip:
                print("strip")
            else:
        #xray = line.split()
        #part = re.search("'/.*']", maybe)
        #if part == maybe:
                count += 1
        #xr = str(xray)
        #print(xr):
                print(eachP)
    print(count)

"""
        for i in line:
                errors.append(line)
                x = line.split()
                print(x)
            



                #strip = jabber.replace("']", " ")
               # print(type(jabber)) str.replace(old, new[, max])
                #part = re.search('/..........................', jabber)
                part = re.search('/.+', jabber)
                if part:
"""




exit(0)
