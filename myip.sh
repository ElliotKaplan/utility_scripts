#!/bin/bash

ipaddr=$(curl -s http://ifconfig.io)
echo $ipaddr
whois $ipaddr \
    | awk -F: '/(Org|Cust)Name/{print $1 "\011"  $2}'


