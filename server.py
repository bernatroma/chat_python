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
    mensaje_cliente = servidor.recv(8)
    print(mensaje_cliente.decode())
    clientConnected.send("Hello"())




    ''''connex, adrr = servidor.accept()
    print("conected by", adrr)
    print("Conection of ",ip, "are accepted")
    mensaje_cliente = .recv()
    print(mensaje_cliente.decode())
    



def recive():
    servidor.accept()
    print("Conection of ",ip, "are accepted")
    recive_mesaje = "als"
    print(recive_mesaje)
    mensaje_cliente = servidor.recv(1024)
    print(mensaje_cliente.decode())
'''
server_con()


