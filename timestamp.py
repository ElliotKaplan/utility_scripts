#!/usr/bin/python3

from datetime import datetime
from argparse import ArgumentParser
import sys

parser = ArgumentParser('convert timestamps into human readable form')
parser.add_argument('timestamps', nargs='+', type=int, help='list of timestamps')
parser.add_argument('-f', '--format', default="%Y-%m-%d %H:%M:%S", type=str, help='format string')
parser.add_argument('-s', '--scale', default=1, type=int, help='scale factor')
clargs = parser.parse_args()

for timestamp in clargs.timestamps:
    timestamp = timestamp / clargs.scale
    print(datetime.fromtimestamp(timestamp).strftime(clargs.format))
