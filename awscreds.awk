#!/usr/bin/awk -f
BEGIN {
    name=ARGV[1];
    ARGV[1]=ENVIRON["HOME"]"/.aws/credentials"
}
($0 ~ name){flag=1; next;}
($0 ~ "^$"){flag=0}
(flag){print "export " toupper($1) $2 $3}

