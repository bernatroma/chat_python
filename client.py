import socket

mensaje = input("What you want to send?")

def client_con_send():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("127.0.0.1", 5555))
    cliente.send(mensaje.encode())
    mensaje_del_server = cliente.recv(1024)
    print(mensaje_del_server.decode())

client_con_send()

    