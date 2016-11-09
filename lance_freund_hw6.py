#!/usr/bin/env python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---

# import urlopen from urllib
from urllib.request import urlopen
from itertools import groupby

# get a copy of file provided as input $1
with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test") as error_sheet:
    errors=[]
    for err in error_sheet:
       # sorted(err)
        line = err.decode('utf-8').split()
        for file in line:
            errors.append(line)
            if line[8] == 'File':
                box = line[12]
                print(box)

exit(0)
