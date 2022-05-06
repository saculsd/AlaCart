from _thread import *
import socket
import sys

server = "192.168.100.147"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("warte auf verbindeungen, Server gestartet")

def threaded_client(conn):
    conn.send(str.encode("test"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("recived: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("connection lost")
    conn.close()

while True:
    conn, addr = s.accept()
    print("verbunden mit", addr)

    start_new_thread(threaded_client, (conn,))