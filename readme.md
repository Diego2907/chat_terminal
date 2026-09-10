EQUIPO 7
Reto: Mensaje privado, usar /msg para enviar un mensaje privado a un usuario

## Cómo correr el proyecto

### Requisitos
- Python 3.x

### Pasos de ejecución

1. **Iniciar el servidor:**
   En una terminal, ejecuta:
   ```bash
   python3 servidor.py
   ```
   El servidor empezará a escuchar conexiones en `localhost:5000`.

2. **Iniciar los clientes:**
   En terminales independientes (una por cada cliente), ejecuta:
   ```bash
   python3 cliente.py
   ```
   El cliente solicitará ingresar un nombre de usuario (debe ser único).

---

## Comandos del cliente

- **`/msg <usuario> <mensaje>`**: Envía un mensaje privado únicamente al usuario especificado.
  - *Ejemplo:* `/msg Juan ¡Hola!`
- **`/salir`** o **`salir`**: Desconecta al cliente del servidor y finaliza el programa (también se puede usar `Ctrl + C`).
- **Mensajes normales (Broadcast)**: Cualquier texto que no comience con `/msg` o `/salir` se transmitirá a todos los demás usuarios conectados.