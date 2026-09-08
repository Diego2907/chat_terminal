# una lista compartida de clientes conectados, para reenviarles el mensaje a todos.
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