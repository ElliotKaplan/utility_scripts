#!/bin/bash

if [ $# -eq 0 ]; then
    echo 'iterpaste.sh <format_str> <values>';
    echo '=======';
    echo 'writes successive values to the clipboard for use in a single paste'
    exit;
fi

# read off the format string
fstring=$1
shift;

for var in $@;
do
    # -loops 3 gets a single paste on dev machine. no idea why
    xclip -loops 3 -verbose -selection clipboard <(printf "$fstring" $var);
done;
