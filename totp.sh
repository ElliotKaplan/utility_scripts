#!/bin/bash

totp=$(xclip -selection clipboard -o | oathtool -b -d6 --totp -)
if [[ $(echo $totp | wc -l) -eq 1 ]]
then
    date
    echo $totp | xclip -selection clipboard
else
    >&2 echo "Clipboard did not contain an OTP key"
    exit 1
fi

