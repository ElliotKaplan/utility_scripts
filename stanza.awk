#!/usr/bin/awk -f 

BEGIN {
    if (ARGC == 0) {
        print("Read a single stanza from a configuration file, defaults to .sshc/onfig");    
        exit;
        }
    if (ARGV[2] == "") {
            ARGV[2] = ENVIRON["HOME"]"/.ssh/config"
        }
    # first argument is the regex. The ARGV stuff is just to make sure
    # only the config file is read
    stanza = ARGV[1];
    ARGV[1] = ARGV[2];
    ARGV[2] = "";
}

($0 ~ stanza){flag=1}
(flag){print $0}
($0 ~ "^$"){flag=0}

