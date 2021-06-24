#!/usr/bin/awk -f

BEGIN {
    if (ARGC == 1) {
        print("Reads in an nmap file and returns a list of ip addresses and ports, separated by colons, specifically to pass to eyewitness for a pass over with a browser");    
        exit;
    }
    
}

($0 ~ "Nmap scan report"){
        host=$NF;
}
($2 == "open"){
    split($1, pt, "/");
    print host ":" pt[1];
}

