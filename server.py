import socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def server_con():
    global ip
    global port
    ip = "127.0.0.1"
    port = 5555
    servidor.bind((ip, port))
    servidor.listen()
    (clientConnected, clientAddress) = servidor.accept()
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
    mensaje_cliente = clientConnected.recv(1024)
    print(mensaje_cliente.decode())
    para_cliente = input("What you want to send?")
    clientConnected.send(para_cliente.encode())

server_con()


