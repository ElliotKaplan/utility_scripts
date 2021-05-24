#!/usr/bin/python3

from subprocess import check_output
from argparse import ArgumentParser

import json
import re

# for converting camel case to underscore separated
camelreg = re.compile('[A-Z][a-z]*')

if __name__=='__main__':
    parser = ArgumentParser('logs into aws for a given profile using MFA')
    parser.add_argument('profile', type=str,
                        help='name of profile in .aws/credentials')
    parser.add_argument('mfa_token', type=str,
                        help='name of token to authenticate against')
    parser.add_argument('token_code', type=str,
                        help='value of time based OTP for token')

    clargs = parser.parse_args()

    resp = check_output(['aws',
                         '--profile', clargs.profile,
                         'sts', 'get-session-token',
                         '--serial-number', clargs.mfa_token,
                         '--token-code', clargs.token_code])
    data = json.loads(resp)
    creds = data['Credentials']
    # remove the expiration as unnecessary
    exp = creds.pop('Expiration')

    # print the shell commands to set the proper environmental
    # variables to use the awscli and/or terraform
    for k, v in creds.items():
        print(
            'export aws_{}={}'.format(
                '_'.join(
                    m.group(0).lower() for m in camelreg.finditer(k)
                ),
                v)
        )
    
    
