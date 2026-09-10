import socket, threading

HOST = "localhost"
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f"Escuchando en el puerto {PORT}")# una lista compartida de clientes conectados, para reenviarles el mensaje a todos.

usuarios = {}
bloqueo = threading.Lock()

def atender_cliente(conexion, direccion):
    #  Registrar al conectarse.
    nombre = conexion.recv(1024).decode().strip()
    
    # Evitar nombres vacíos.
    if not nombre:
        conexion.send("ERROR: debes escribir un nombre".encode())
        conexion.close()
        return
 
    # Registrar al usuario.
    with bloqueo:
        if nombre in usuarios:
            conexion.send("ERROR: ese nombre ya esta en uso".encode())
            conexion.close()
            return
        
        usuarios[nombre] = conexion
 
    # Respuesta al cliente.
    conexion.send(f"OK: bienvenido {nombre}".encode())
    print(f"{nombre} conectado desde {direccion}")
 
    try:
        while True:
            datos = conexion.recv(1024)

            if not datos:
                break

            texto = datos.decode().strip()

            if not texto:
                continue

            # Cerrar la conexión cuando el usuario escribe /salir
            if texto.lower() == "/salir":
                break
 
            # mensaje privado
            if texto == "/msg" or texto.startswith("/msg "):
                partes = texto.split(" ", 2)

                # Validar que tenga comando, usuario y mensaje.
                if len(partes) < 3:
                    conexion.send(
                        "ERROR: uso /msg <usuario> <mensaje>".encode()
                    )
                    continue
 
                destinatario = partes[1]
                privado = partes[2]
 
                with bloqueo:
                    destino = usuarios.get(destinatario)
 
                if destino is None:
                    conexion.send(
                        f"ERROR: {destinatario} no esta conectado".encode()
                    )
                else:
                    try:
                        destino.send(
                            f"[privado de {nombre}] {privado}".encode()
                        )
                        conexion.send(
                            f"[privado para {destinatario}] {privado}".encode()
                        )
                    except OSError:
                        conexion.send(
                            f"ERROR: no se pudo enviar el mensaje a "
                            f"{destinatario}".encode()
                        )
 
            # El broadcast a todos menos a mi
            else:
                mensaje = f"{nombre}: {texto}"

                with bloqueo:
                    destinos = list(usuarios.values())

                for cliente in destinos:
                    if cliente != conexion:
                        try:
                            cliente.send(mensaje.encode())
                        except OSError:
                            pass
 
    except (ConnectionResetError, OSError):
        print(f"{nombre} se desconecto mal")

    finally:
        with bloqueo:
            usuarios.pop(nombre, None)

        conexion.close()
        print(f"{nombre} desconectado")
 
 
while True:
    conexion, direccion = servidor.accept()
    print(f"Nuevo Hilo {direccion}")
 
    hilo = threading.Thread(
        target=atender_cliente,
        args=(conexion, direccion)
    )

    hilo.start()