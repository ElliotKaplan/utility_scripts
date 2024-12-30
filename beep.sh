#!/bin/bash

speaker-test -t sine -f 1000 -l 0.5 >/dev/null &
sleep 0.1;
kill -9 $(pidof speaker-test);
