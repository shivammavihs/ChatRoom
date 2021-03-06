from os import name
import socket
from threading import Thread

def send_msg(c,name_c):
    while True:
        msg = input()
        c.send(msg.encode())

def recv_msg(c,name_c):
    while True:
        try:
            msg = c.recv(1024).decode()
            print(msg)
        except:
            c.close()
            break

def create_client(s_ip):
    name_c = input('Enter your name: ')
    if s_ip == '': s_ip = input('Enter the server ip: ')
    c = socket.socket()
    c.connect((s_ip,9999))
    c.send(name_c.encode())
    print(c.recv(1024).decode())
    t1 = Thread(target=send_msg, args=(c,name_c))
    t1.start()
    t2 = Thread(target=recv_msg, args=(c,name_c))
    t2.start()



