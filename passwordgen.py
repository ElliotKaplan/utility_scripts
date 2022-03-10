#!/usr/bin/python3

from random import choice
from string import ascii_uppercase, ascii_lowercase, digits

from argparse import ArgumentParser


argparser = ArgumentParser('generates a random password')
argparser.add_argument('-n', '--nchars', type=int, default=16,
                       help='number of characters')
argparser.add_argument('-r', '--range', nargs=2, default=(0x21, 0x80),
                       help='range of possible values')
argparser.add_argument('-d', '--digits', action='store_true',
                       help='only output digits')
argparser.add_argument('--no_special', action='store_true',
                       help='set to not include special characters')
argparser.add_argument('--xkcd', action='store_true',
                       help='set to use /usr/share/dict/american-english to seed a password')
argparser.add_argument('--xkcd_hard', action='store_true',
                       help='like xkcd but with one random capital and one digit')


clargs = argparser.parse_args()
if clargs.digits:
    chrs = digits
elif clargs.no_special:
    chrs = ascii_lowercase + ascii_uppercase + digits
elif clargs.xkcd or clargs.xkcd_hard:
    with open('/usr/share/dict/american-english') as fi:
        chrs = list(set(map(lambda s: s.strip('\n').strip("'s").capitalize(), fi)))
else:
    chrs = list(map(chr, range(*map(int, clargs.range))))


# add an extra digit into the middle of an xkcd style password
if clargs.xkcd_hard:
    words = [choice(chrs) for _ in range(clargs.nchars)]
    # capitalize one random character
    ind = choice(list(range(clargs.nchars)))
    cap = choice(list(range(len(words[ind]))))
    words[ind] = words[ind][:cap] + words[ind][cap].upper() + words[ind][cap+1:]

    # insert one random digit
    ind = choice(list(range(clargs.nchars)))
    dig = choice(digits)
    # require the digit in the middle of the word
    ins = choice(list(range(1, len(words[ind])-1)))
    words[ind] = words[ind][:ins] + dig + words[ind][ins:]
    passwd = ''.join(words)
    
else:
    passwd = ''.join(choice(chrs) for _ in range(clargs.nchars))

    
print(passwd)
