import socket
import threading

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 5000))


def crear_usuario(nombre_usuario):
    cliente.send(nombre_usuario.encode())
    respuesta = cliente.recv(1024).decode()
    print(f"Servidor dice: {respuesta}")
    return respuesta


def recibir_mensajes():
    """Corre en segundo plano imprimiendo lo que llega del servidor."""
    while True:
        try:
            datos = cliente.recv(1024)
            if not datos:
                print("\n[Conexion cerrada por el servidor]")
                break
            print(f"\n{datos.decode()}\n> ", end="", flush=True)
        except OSError:
            break


def mensaje():
    """Bucle principal: lee del teclado y manda al servidor."""
    while True:
        try:
            texto = input("> ")
        except (EOFError, KeyboardInterrupt):
            texto = "/salir"

        if not texto.strip():
            continue

        if texto.lower() in ("/salir", "salir"):
            cliente.send("/salir".encode())
            break

        # /msg y texto normal se mandan igual: el servidor es quien parsea.
        # Aqui solo validamos el formato para avisar antes de enviar.
        if texto.startswith("/msg " ) or texto.startswith("/msg"):
            partes = texto.split(" ", 2)
            if len(partes) < 3:
                print("Uso del comando: /msg <usuario> <mensaje>")
                continue

        cliente.send(texto.encode())


# --- Arranque ---
nombre = input("Escribe tu nombre de usuario: ").strip()
respuesta = crear_usuario(nombre)

if respuesta.startswith("ERROR"):
    print("No se pudo registrar. Cerrando.")
    cliente.close()
else:
    # 1) El hilo receptor va en segundo plano
    hilo_recibir = threading.Thread(target=recibir_mensajes, daemon=True)
    hilo_recibir.start()

    # 2) El bucle de entrada va en el hilo PRINCIPAL: es lo que
    #    mantiene vivo el programa. Antes faltaba esta llamada.
    try:
        mensaje()
    finally:
        cliente.close()
        print("Desconectado.")