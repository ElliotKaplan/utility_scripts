#!/bin/bash

if [ $# -eq 0 ]; then
    echo 'archivedir.sh target_dir';
    echo '=======';
    echo 'tarballs a directory and labels it with the username. gzips the subsequent .tar file';
    echo 'subsequent file is $(target_dir)_$(whoami)_working_directory.tar.gz';
    exit;
fi

targ=$1
if [ ! -d "$targ" ]; then
    echo "target_dir needs to be a directory";
    exit;
fi
    
echo "original";
du -h $targ --max-depth 0;

dest=$targ\_$(whoami)\_working_directory.tar;

tar -cf $dest $targ && gzip $dest;

echo "";
echo "compressed size";
du -h "$dest.gz" -h;

