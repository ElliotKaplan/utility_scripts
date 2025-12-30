#!/usr/bin/python3
def setops(a_file, b_file, op='union', sep=None):
    a = set(a_file.read().split(sep))
    b = set(b_file.read().split(sep))
    return getattr(a, op)(b)
    

if __name__ == "__main__":
    from argparse import ArgumentParser, FileType
    import sys

    argparser = ArgumentParser('performs set operations on files')
    argparser.add_argument('operation', type=str, choices=['union', 'intersection', 'difference', 'symmetric_difference'],
                           help='set operation to perform')
    argparser.add_argument('set_a', type=FileType('r'), help='first set')
    argparser.add_argument('set_b', type=FileType('r'), default=sys.stdin,
                           help='second set, can be read from stdin')

    argparser.add_argument('-s', '--sep', type=str, default='\n',
                           help='seperator')
    clargs = argparser.parse_args()
    print('\n'.join(setops(clargs.set_a, clargs.set_b, clargs.operation, sep=clargs.sep)))
