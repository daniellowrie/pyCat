#!/usr/bin/env python3

import sys
import socket

RHOST = sys.argv[1]             # The server's hostname or IP address
RPORT = int(sys.argv[2])        # The port used by the server

def sender():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((RHOST, RPORT))
        while True:
            cmds = input('~pyCat Client~$ ').encode()
            s.sendall(cmds)
            data = s.recv(1024)
            print (data.decode())
            main()

def main():
    sender()

main()
