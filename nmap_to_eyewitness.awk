#!/usr/bin/awk -f

BEGIN {
    if (ARGC == 1) {
        print("Reads in an nmap file and returns a list of ip addresses and ports intended for passing to an eyewitness script");
        exit;
    }
}

($0 ~ "Nmap scan report"){
    host=$NF;
}
($2 == "open"){
    split($1, port, "/");
    # drop any port under 1000, excepting 80 and 443 as unlikely to be
    # http services
    if ((port[1] < 1000) && (port[1] != 80) && (port[1] != 443)) next;
      if ($3 ~ "ssl") {
        pref = "https://"
    }
    else {
        pref = "http://"
    };
    print(pref host ":" port[1]);
}
