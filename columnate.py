#!/usr/bin/python3

import math

def columnate(ncol, *args, sep='\t', column=None):
    nrow = math.ceil(len(args) / ncol)
    cols = [list(s.strip() for s in args[i*nrow:(i+1)*nrow])
            for i in range(ncol)]
    for col in cols[1:]:
        while(len(col) != len(cols[0])):
            col.append('')
    if column is None:
        return '\n'.join(sep.join(r) for r in zip(*cols))
    return '\n'.join(cols[column])
    

if __name__=='__main__':
    from argparse import ArgumentParser, FileType
    argparser = ArgumentParser('split input into columns')
    argparser.add_argument('-nc', '--num_col', type=int, default=3,
                           help='number of columns')
    argparser.add_argument('-s', '--separator', type=str, default='\t',
                           help='column separator')
    argparser.add_argument('-c', '--column', type=int, default=None,
                           help='which column to print, default all')
    argparser.add_argument('input', nargs='?', default='-', type=FileType('r'),
                           help='inputdata, default is stdin')

    clargs = argparser.parse_args()
    print(columnate(clargs.num_col, *clargs.input, sep=clargs.separator, column=clargs.column))

