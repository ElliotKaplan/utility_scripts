#!/bin/bash

if [ $# -eq 0 ]; then
    echo 'todaydir.sh basename';
    echo '=======';
    echo "makes a directory labeled with today's date";
    echo 'subsequent directory is YYYY_MM_DD_basename';
    exit;
fi


mkdir "$(date '+%Y_%m_%d')_$1"
