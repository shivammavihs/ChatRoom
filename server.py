import socket
from threading import Thread
from time import sleep, time

def message_exchange(c, clients):
    while True:
        try:
            msg = c.recv(1024).decode()
            if msg.lower() == 'exit':
                raise Exception
            for i in clients:
                if i == c:
                    i.send(('You: '+msg).encode())
                else:
                    i.send((clients[c]+': '+msg).encode())
        except Exception:
            for i in clients:
                if i != c:
                    i.send((f'{clients[c]} left the chat room.').encode()) 
            del clients[c]
            c.close()
            break    

def create_server():
    s = socket.socket()
    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)
    s.bind((host_name,9999))

    s.listen(4)

    clients = {}
    flag = 'y'
    while True:
        c, addr = s.accept()
        name = c.recv(1024).decode()
        clients[c] = name
        if flag == 'y':
            s_name = name
            flag = 'n'
            c.send(('You created the chat room').encode())
            c.send((f'Server IP: {s_ip}. Share with your friends to connect.').encode())
            sleep(0.1)
            c.send(('Waiting for members').encode())
            
        else:
            c.send((f'{s_name} is the admin of this chat room.').encode())
            c.send((f'You joined the chat room.').encode())
            for i in clients:
                if i != c:
                    i.send((f'{name} joined the chat room.').encode())
        
        t1 = Thread(target=message_exchange, args=(c, clients))
        t1.start()