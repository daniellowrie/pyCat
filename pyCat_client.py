#!/usr/bin/env python3

import sys
import socket

RHOST = sys.argv[1]             # The server's hostname or IP address
RPORT = int(sys.argv[2])        # The port used by the server

def sender():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((RHOST, RPORT))
        while True:
            stderr = (' 2>&1')
            userin = input('~pyCat Client~$ ')
            cmds = (userin + stderr).encode()
            s.sendall(cmds)
            data = s.recv(65536)
            print (data.decode())
            main()

def main():
    sender()

main()
