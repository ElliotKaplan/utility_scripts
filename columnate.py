#!/usr/bin/python3

import math

def columnate(ncol, *args, sep='\t'):
    nrow = math.ceil(len(args) / ncol)
    cols = [list(s.strip() for s in args[i*nrow:(i+1)*nrow])
            for i in range(ncol)]
    for col in cols[1:]:
        while(len(col) != len(cols[0])):
            col.append('')
    print('\n'.join(sep.join(r) for r in zip(*cols)))
    

if __name__=='__main__':
    from argparse import ArgumentParser, FileType
    argparser = ArgumentParser('split input into columns')
    argparser.add_argument('-nc', '--num_col', type=int, default=3,
                           help='number of columns')
    argparser.add_argument('-s', '--separator', type=str, default='\t',
                           help='column separator')
    argparser.add_argument('input', nargs='?', type=FileType('r'),
                           help='inputdata, set to "-" for stdin')

    clargs = argparser.parse_args()
    columnate(clargs.num_col, *clargs.input, sep=clargs.separator)

