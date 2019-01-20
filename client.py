#!/usr/bin/env python
import socket
import sys
import argparse
host='localhost'
def echo_client(port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address=(host, port)
    print("Connecting to %s port %s server_address " % server_address)
    sock.connect(server_address)

    try:
        message="Test Message"
        print("Sending %s " % message)
        sock.sendall(message.encode('utf-8'))
        amntRecvd=0
        amntExpctd=len(message)
        while amntRecvd<amntExpctd:
            data=sock.recv(16)
            amntRecvd+=len(data)
            print("Received %s " % data)
    except socket.error as e:
        print("Socket error %s "% str(e))
    except Exception as e:
        print("Exception %s " % str(e))
    finally:
        print("Closing connection to server")

if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Sockets")
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    give_args=parser.parse_args()
    port=give_args.port
    echo_client(port)
