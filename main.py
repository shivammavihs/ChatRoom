import client
import server
from threading import Thread
import time
import socket

def create_server():
    try:
        server.create_server()
    except Exception:
        print('Already a server is running, try joining it')
        choice()
        
def create_client(s_ip):
    try:
        client.create_client(s_ip)
    except Exception:
        print('There is no online server, try creating one.')
        choice()

def choice():
    print('''
Welcome to the chat room

1. Enter 1 to Create a room.
2. Enter 2 to join a room.''')

    choice = int(input())
    if choice == 1:
        t1 = Thread(target=create_server)
        t1.start()
        time.sleep(0.2)
        host_name = socket.gethostname()
        s_ip = socket.gethostbyname(host_name)
        t2 = Thread(target=create_client,args=(s_ip,))
        t2.start()
    elif choice == 2:
        create_client('')

choice()