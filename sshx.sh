#!/bin/bash

# modification of https://xicod.com/2021/02/09/clipboard-over-ssh.html to run as a separate shell script instead of as part of the .bashrc

_dt_socket_ssh() {
    ssh -oControlPath=$1 -O exit DUMMY_HOST
}

sshx() {
    chars="0123456789abcdef";
    local t=$(mktemp -u --tmpdir "ssh.sock.XXXXXXXX");
    local f="~/clip";
    ssh -f -oControlMaster=yes -oControlPath=$t $@ tail\ -f\ /dev/null || return 1;
    ssh -S$t DUMMY_HOST "bash -c 'if ! [ -p $f ]; then mkfifo $f; fi'" \
        || { _dt_term_socket_ssh $t; return 1; }
    (
        set -e
        set -o pipefail
        while [ 1 ]; do
            ssh -S$t -tt DUMMY_HOST "cat $f" 2>/dev/null | xclip -selection clipboard
            done &
    )
    ssh -S$t DUMMY_HOST \
        || { _dt_term_socket_ssh $t; return 1; }
    ssh -S$t DUMMY_HOST "command rm $f"
    _dt_term_socket_ssh $t
}

sshx $@
