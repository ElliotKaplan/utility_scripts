#! /usr/bin/python3 

import sys

import aiohttp
import asyncio
from bs4 import BeautifulSoup, Comment

host = 'https://nvd.nist.gov/vuln/detail/'

async def main(cvelist):
    async with aiohttp.ClientSession() as sess:
        for cve in cvelist:
            cve = cve.strip()
            async with sess.get(f'{host}{cve}') as resp:
                if resp.status != 200:
                    continue
                try:
                    body = await resp.text()
                    soup = BeautifulSoup(body, 'lxml')

                    # get the cvss score
                    scoretag = soup.find(
                        'a', attrs={'id': 'Cvss3NistCalculatorAnchor'}
                    )
                    score = scoretag.text.split()
                    vectag = soup.find(
                        'span', attrs={'class': 'tooltipCvss3NistMetrics'}
                    )
                    print(f'{cve}\t{score[1]} {score[0]} {vectag.text}')
                # ignore failed searches
                except AttributeError:
                    continue
                    
                    
if __name__ == '__main__':
    from argparse import ArgumentParser, FileType

    parser = ArgumentParser('search cvefeed.io for public exploits')

    parser.add_argument('cves', nargs='?', default='-', type=FileType('r'),
                           help='cves to search for exploits for, default is stdin')

    clargs = parser.parse_args()
    asyncio.run(main(clargs.cves))
