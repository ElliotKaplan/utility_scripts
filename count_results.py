#!/usr/bin/python3

from collections import Counter
import sys
import math
from argparse import ArgumentParser

if __name__=='__main__':
    argparser = ArgumentParser('count unique results from stdin')
    argparser.add_argument('-u', '--unique', action='store_true',
                           help='set to only print unique values')
    argparser.add_argument('-d', '--descending', action='store_true',
                           help='set to sort output by count descending')
    argparser.add_argument('-a', '--alphasort', action='store_true',
                           help='set to sort output alphabetially')
    argparser.add_argument('-t', '--total', action='store_true',
                           help='set to output a total count alongside individual values')
    argparser.add_argument('--to_upper', action='store_true',
                           help='set to convert values to upper case before counting')
    argparser.add_argument('--to_lower', action='store_true',
                           help='set to convert values to lower case before counting')

    clargs = argparser.parse_args()
    stream = sys.stdin
    if clargs.to_upper:
        stream = map(lambda s: s.upper(), stream)
    if clargs.to_lower:
        stream = map(lambda s: s.lower(), stream)

    if clargs.unique:
        vals = set(stream)
        for val in sorted(vals, reverse=clargs.descending):
            print(val.strip())
        sys.exit()

    cnt = Counter(stream)
    sortind = {True: 0, False: 1}[clargs.alphasort]
    maxdig = math.floor(
        max(map(math.log, cnt.values()))
        / math.log(10)) + 1

    fmtstr = '{:>' + str(maxdig) + 'd}' + 5*' ' + '{}'
    for k, v in sorted(cnt.items(), key=lambda t: t[sortind], reverse=clargs.descending):
        print(fmtstr.format(v, k.strip()))
    if clargs.total:
        print('='*(maxdig + 4 + max(map(len, cnt.keys()))))
        print(fmtstr.format(sum(cnt.values()), ''))

