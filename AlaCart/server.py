from _thread import *
import socket
import sys
import pickle



server = "192.168.100.147"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("warte auf verbindeungen, Server gestartet")



liste = ["ready-not"]

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
                    print(liste[0])

                if data == "ready" or liste[0] == "ready":
                    reply = "ready-ok"
                    liste[0] = "ready"
                    print(liste)





                #print("recived: ", data)
                #print("Sending: ", reply)

                conn.sendall(pickle.dumps(reply))


        except:
            break

    print("connection lost")
    list[0] = "ready-not"
    conn.close()

def connect():

    currentPlayer = 1

    while True:
        conn, addr = s.accept()
        print("verbunden mit: ", addr)
        print(currentPlayer)
        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1



connect()