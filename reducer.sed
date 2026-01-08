#!/usr/bin/sed -f

/^[;#]/d;
/^$/d;
p;d; # can't set -n for some reason