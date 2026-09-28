#!/usr/bin/python3

from subprocess import Popen, PIPE
from argparse import ArgumentParser, FileType
from os import path
import itertools
import sys
def dnscheck(domain, fobj, dnsserver='127.0.0.53', nsubdomains=50, scrapetop=False):
    if scrapetop:
        fqdn_gen = (
            ['.'.join((domain, s.strip())) for s in b]
            for b in itertools.batched(fobj, nsubdomains)
        )
    else:
        fqdn_gen = (
            ['.'.join((s.strip(), domain)) for s in b]
            for b in itertools.batched(fobj, nsubdomains)
        )
    
    for fqdns in fqdn_gen:
        # make the queries to the target dns server
        p1 = Popen(['dig', '@'+dnsserver] + fqdns,
                   stdout=PIPE)
        # process the output and grab the valid domains
        # it's just easier with awk
        p2 = Popen(['awk', '($4=="A" || $4 =="CNAME"){print $1 "," $5}'],
                   stdin=p1.stdout, stdout=PIPE)
        p1.stdout.close()
        out = p2.communicate()[0].decode()
        
        yield out

argparser = ArgumentParser('find valid subdomains')
argparser.add_argument('domain', type=str,
                       help='domain to enumerate')
argparser.add_argument('subdomainlist', type=FileType('r'), nargs='?', default='-',
                       help='filetype containing subdomains')
argparser.add_argument('-t', '--scrapetop', action='store_true',
                       help='set to iterate over interior domain names')
argparser.add_argument('-d', '--dnsserver', type=str, default='127.0.0.53',
                       help='server to query')
argparser.add_argument('-c', '--chunksize', type=int, default=50,
                       help='number of subdomains to check at once')

if __name__=='__main__':
    clargs = argparser.parse_args()
    for i, out in enumerate(
            dnscheck(
                clargs.domain, clargs.subdomainlist,
                dnsserver=clargs.dnsserver,
                nsubdomains=clargs.chunksize,
                scrapetop=clargs.scrapetop
            )):
        print(out, end='')

