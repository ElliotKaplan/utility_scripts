#!/usr/bin/python3
from netaddr import ip

def ipsort(stream, reverse=False):
    return sorted(map(lambda s: s.strip(), stream), key=ip.IPAddress, reverse=reverse)

if __name__ == '__main__':
    # import fileinput
    # print('\n'.join(ipsort( fileinput.input())))
    from argparse import ArgumentParser, FileType
    import sys
    argparser = ArgumentParser('sort a stream or file by ip address')
    argparser.add_argument('infile', nargs='?',
                           type=FileType('r'),
                           default=sys.stdin)
    argparser.add_argument('-r', '--reverse', action='store_true',
                           help='set to reverse sort order')
    clargs = argparser.parse_args()
    print('\n'.join(ipsort(clargs.infile, reverse=clargs.reverse)))
