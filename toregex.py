#!/usr/bin/python3

if __name__ == '__main__':
    from argparse import ArgumentParser, FileType
    import sys
    argparser = ArgumentParser('convert a stream or file into a PERL style regex')
    argparser.add_argument('infile', nargs='?',
                           type=FileType('r'),
                           default=sys.stdin)

    clargs = argparser.parse_args()
    print('|'.join(map(lambda s: s.strip(), clargs.infile)).join('()'))
