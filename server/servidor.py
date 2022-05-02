import socket 
import threading

def criptografia(palavra):
    zenit, polar = 'zenit' , 'polar'
    final_message = ''
    message = palavra
    n = 0
    for i in range(len(message)):
        x = message[n]
        if x in zenit:
            x = int(zenit.find(message[n]))
            final_message += polar[x]
        elif x in polar:
            x = int(polar.find(message[n]))
            final_message += zenit[x]
        else:
            final_message += message[n]
        n += 1
    return final_message



HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname('127.0.0.1')
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT = "sair"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def atender_client(conn, addr):
    print("[NOVA CONEXAO] ",addr," Conectado ")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONECT:
                connected = False
            num = criptografia(msg)
            print(addr," Digitou: ", msg)
            conn.send((num).encode(FORMAT))
    conn.close()  

def start():
    server.listen()
    print("[OUVINDO] O servidor esta ouvindo no endereco:", SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=atender_client, args=(conn, addr))
        thread.start()
        print("[CONEXOES ATIVAS]" , threading.activeCount() - 1)
print("[INICIADO] O SERVIDOR ESTA INICIADO...")

start()