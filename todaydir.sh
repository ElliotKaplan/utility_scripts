#!/bin/bash

if [ $# -eq 0 ]; then
    echo 'todaydir.sh basename';
    echo '=======';
    echo "makes a directory labeled with today's date";
    echo 'subsequent directory is YYYY_MM_DD_basename';
    exit;
fi

targetdir="$(date '+%Y_%m_%d')_$1"
mkdir $targetdir
cd $targetdir

# set up directories
mkdir client_data
mkdir scan_output
mkdir screenshots
mkdir scripts
mkdir sqlmap
# need some python fluff
touch scripts/__init__.py
touch sqlmap/__init__.py
# set up a place to log all the command line stuff
# set to append only so that you don't accidentally overwrite it
touch commandlog && sudo chattr +a commandlog

# basic todo list
cat <<EOF > notes.org
#+title:  $1
#+author: $(whoami)
#+date:   $(date '+%Y-%m-%d')

* TODO Setup
** TODO review client docs
** TODO set up burp configuration

* TODO Unauthenticated Scans
** TODO Port Scan
** TODO DNS enumeration
** TODO TLS Cipher Suite
** TODO dirsearch scan

* TODO Authenticated Scans
** TODO script logon
** TODO Remove logoff from scope
** TODO authenticated dirsearch
** TODO Burp active scan

 
EOF
