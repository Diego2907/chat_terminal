import socket, threading
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 5000))
servidor.listen()
print("Escuchando en el puerto 5000")# una lista compartida de clientes conectados, para reenviarles el mensaje a todos.

clientes_conectados = []

def atender_cliente(conexion, direccion):
    clientes_conectados.append(conexion)
    try:
        while True:
            datos = conexion.recv(1024)
            if not datos:
                break
            mensaje = f"{direccion}: {datos.decode()}"
            for cliente in clientes_conectados:
                if cliente != conexion:
                    cliente.send(mensaje.encode())
    except ConnectionResetError:
        print(f"{direccion} se desconectó mal")
    finally:
        clientes_conectados.remove(conexion)
        conexion.close()
        
while True:
    conexion, direccion = servidor.accept()
    print(f"Nuevo Hilo {direccion}, ")

    hilo = threading.Thread(target=atender_cliente, args=(conexion, direccion))
    hilo.start()