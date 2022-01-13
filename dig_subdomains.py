#!/usr/bin/python3

from subprocess import Popen, PIPE
from argparse import ArgumentParser
from os import path

def dnscheck(domain, fobj, dnsserver='127.0.0.53', nsubdomains=50):
    eof = path.getsize(fobj.name)
    subdoms = 'start'
    while True:
        subdoms = [
            '.'.join((s.strip(), domain))
            for _, s in zip(range(nsubdomains), fobj)
        ]
        # make the queries to the target dns server
        p1 = Popen(['dig', '@'+dnsserver] + subdoms,
                   stdout=PIPE)
        # process the output and grab the valid domains
        # it's just easier with awk
        p2 = Popen(['awk', '($4=="A" || $4 =="CNAME"){print $1 "," $5}'],
                   stdin=p1.stdout, stdout=PIPE)
        p1.stdout.close()
        out = p2.communicate()[0].decode()
        
        yield out
        if len(subdoms) == 0:
            break

argparser = ArgumentParser('find valid subdomains')
argparser.add_argument('domain', type=str,
                       help='domain to enumerate')
argparser.add_argument('subdomainlist', type=str,
                       help='filename containing subdomains')
argparser.add_argument('-d', '--dnsserver', type=str, default='127.0.0.53',
                       help='server to query')
argparser.add_argument('-c', '--chunksize', type=int, default=50,
                       help='number of subdomains to check at once')

if __name__=='__main__':
    clargs = argparser.parse_args()
    with open(clargs.subdomainlist) as fi:
        for i, out in enumerate(dnscheck(clargs.domain, fi,
                            dnsserver=clargs.dnsserver,
                            nsubdomains=clargs.chunksize)):
            print(out, end='')

