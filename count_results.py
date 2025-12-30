#!/usr/bin/python3

from collections import Counter
import sys
import math
from argparse import ArgumentParser, FileType

argparser = ArgumentParser('count unique results from stdin')
argparser.add_argument('stream', type=FileType('r'), nargs='?', default=sys.stdin,
                       help='file to count, defaults to stdin')
argparser.add_argument('-u', '--unique', action='store_true',
                       help='set to only print unique values')
argparser.add_argument('-n', '--nosort', action='store_true',
                       help='set to retain the order of the unique entries')
argparser.add_argument('-d', '--descending', action='store_true',
                       help='set to sort output by count descending')
argparser.add_argument('-a', '--alphasort', action='store_true',
                       help='set to sort output alphabetially')
argparser.add_argument('-t', '--total', action='store_true',
                       help='set to output a total count alongside individual values')
argparser.add_argument('-s', '--stream', action='store_true',
                       help='set to stream live results as they come in. Specific to unique')
argparser.add_argument('--sep', default='\n',
                       help='set to change separator between values. Specific to unique')
argparser.add_argument('--to_upper', action='store_true',
                       help='set to convert values to upper case before counting')
argparser.add_argument('--to_lower', action='store_true',
                       help='set to convert values to lower case before counting')
argparser.add_argument('-m', '--minimum', type=int, default=-1,
                       help='set to have a minimum number of entries before being printed')
argparser.add_argument('--header', action='store_true',
                       help='set to print column headers')


if __name__=='__main__':

    clargs = argparser.parse_args()
    stream = clargs.stream
    if clargs.to_upper:
        stream = map(lambda s: s.upper(), stream)
    if clargs.to_lower:
        stream = map(lambda s: s.lower(), stream)

    if clargs.unique:
        vals = set(stream)
        print(
            clargs.sep.join(
                sorted(
                    (v.strip() for v in vals),
                    reverse=clargs.descending
                )
            )
        )
        sys.exit()

    if clargs.nosort:
        first = dict()
        for i, val in enumerate(stream):
            first[val] = first.get(val, i)
        ordval = {v: k for k, v in first.items()}
        for i in sorted(ordval.keys()):
            print(ordval[i].strip())
        sys.exit()

    cnt = Counter(stream)
    sortind = {True: 0, False: 1}[clargs.alphasort]
    maxdig = math.floor(
        max(map(math.log, cnt.values()))
        / math.log(10)) + 1

    fmtstr = '{:>' + str(maxdig) + 'd}' + 5*' ' + '{}'
    if clargs.header:
        print(('{:>' + str(maxdig) + 's}     {}').format('Count', 'Value'))
        
    for k, v in sorted(cnt.items(), key=lambda t: t[sortind], reverse=clargs.descending):
        if v >= clargs.minimum:
            print(fmtstr.format(v, k.strip()))
    if clargs.total:
        print('='*(maxdig + 4 + max(map(len, cnt.keys()))))
        print(fmtstr.format(sum(cnt.values()), ''))

