#!/bin/bash

ipaddr=$(curl -s http://ifconfig.io)

org=$(whois $ipaddr | awk -F: '/OrgName/{print $2}')

echo $ipaddr " "  $org

