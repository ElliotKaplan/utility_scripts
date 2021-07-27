#!/usr/bin/python3

from random import choice
from string import ascii_uppercase, ascii_lowercase, digits

from argparse import ArgumentParser


argparser = ArgumentParser('generates a random password')
argparser.add_argument('-n', '--nchars', type=int, default=16,
                       help='number of characters')
argparser.add_argument('-r', '--range', nargs=2, default=(0x21, 0x80),
                       help='range of possible values')
argparser.add_argument('-d', '--digits', action='store_true',
                       help='only output digits')
argparser.add_argument('--no_special', action='store_true',
                       help='set to not include special characters')

clargs = argparser.parse_args()
if clargs.digits:
    clargs.range = (0x30, 0x39)
if clargs.no_special:
    chrs = ascii_lowercase + ascii_uppercase + digits
else:
    chrs = list(map(chr, range(*map(int, clargs.range))))


print(''.join(choice(chrs) for _ in range(clargs.nchars)))
