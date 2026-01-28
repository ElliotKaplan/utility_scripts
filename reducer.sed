#!/usr/bin/sed -f

/^[;#]/d; # common comments
/^$/d;  # empty lines
p;d; # can't set -n for some reason