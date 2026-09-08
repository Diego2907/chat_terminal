import socket
import threading

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #①
cliente.connect(("localhost", 5000))                    #②


def crear_usuario(nombre_usuario):
    cliente.send(nombre_usuario.encode())
    respuesta = cliente.recv(1024).decode()
    print(f"Servidor dice: {respuesta}")
    return respuesta


def mensaje_privado(destinatario, mensaje):
    cliente.send(f"/msg {destinatario} {mensaje}".encode())


def recibir_mensajes():
    while True:
        try:
            datos = cliente.recv(1024)
            if not datos:
                break
            print(f"\n{datos.decode()}\n> ", end="", flush=True)
        except Exception:
            break


def mensaje():
    while True:
        texto = input("Escribe un mensaje para el servidor: ")
        if not texto:
            continue
        if texto.startswith("/msg"):
            partes = texto.split(" ", 2)
            if len(partes) >= 3:
                mensaje_privado(partes[1], partes[2])
            else:
                print("Uso: /msg <usuario> <mensaje>")
        elif texto.lower() in ["/salir", "salir"]:
            cliente.send("/salir".encode())
            break
        else:
            cliente.send(texto.encode())


crear_usuario("prueba")

hilo_recibir = threading.Thread(target=recibir_mensajes, daemon=True)
hilo_recibir.start()