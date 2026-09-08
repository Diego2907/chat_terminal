import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #①
cliente.connect(("localhost", 5000))                    #②

cliente.send("prueba".encode())                  #③
respuesta = cliente.recv(1024).decode()
print(f"Servidor dice: {respuesta}")

def mensaje():
    while True:
        mensaje = input("Escribe un mensaje para el servidor: ")
        cliente.send(mensaje.encode())
        respuesta = cliente.recv(1024).decode()
        print(f"Servidor dice: {respuesta}")