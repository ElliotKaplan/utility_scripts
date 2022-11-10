#!/usr/bin/python3

from itertools import chain
import sys

if sys.argv[1].startswith('-o'):
    for char in chain(*sys.argv[2:]):
        print(char, "\t", oct(ord(char)))
    sys.exit()
    
if sys.argv[-1].startswith('-o'):
    for char in chain(*sys.argv[1:-1]):
        print(char, "\t", oct(ord(char)))
    sys.exit()

for char in chain(*sys.argv[1:]):
    print(char, "\t", hex(ord(char)))
