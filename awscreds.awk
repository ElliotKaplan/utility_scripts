#!/usr/bin/awk -f
BEGIN {
    if (ARGC == 1) {
        print("awscreds.awk profilename");
        print("\011Use to set environmental variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY for a specific profile.");
        exit;
    }
    name=ARGV[1];
    ARGV[1]=ENVIRON["HOME"]"/.aws/credentials"
}
($0 ~ name){flag=1; next;}
($0 ~ "^$"){flag=0}
(flag){print "export " toupper($1) $2 $3}

