#!/usr/bin/python3

from itertools import chain
import sys

for char in chain(*sys.argv[1:]):
    print(char, "\t", hex(ord(char)))
