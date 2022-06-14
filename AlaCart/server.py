import dis
from _thread import *
import socket
import sys
import pickle
from network import Disconnect



server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("warte auf verbindeungen, Server gestartet")



d = Disconnect()


def threaded_client(conn, player):

    conn.send(pickle.dumps(player))
    reply = 0
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            #print(data)

            if not data:
                print("Disconnected")
                break

            else:




                if data == "wait":
                    reply = "wait-ok"

                if data == "ready" and d.disconnect == False:
                    reply = "ready-ok"
                    d.ready = True

                elif d.ready == True and d.disconnect == False:
                    reply = "ready-ok"

                else:
                    reply = "wait-ok"


                print("recived: ", data)
                print("Sending: ", reply)

                conn.sendall(pickle.dumps(reply))


        except Exception as e:
            print(e)
            break

    print("connection lost")
    if d.disc() == True:
        d.all_disconnect = True
        d.ready = False


    d.disconnect = True
    conn.close()


currentPlayer = 1

while True:
    conn, addr = s.accept()

    if d.disc() == True:
        currentPlayer -= 1
        d.disconnect = False
        if d.all_disc() == True:
            currentPlayer -= 1
            d.all_disconnect = False

    print("verbunden mit: ", addr, f" spieler -> {currentPlayer}")
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1



