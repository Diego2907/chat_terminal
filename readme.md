# Equipo 7 — Chat Broadcast

## Integrantes

- Lorenzo
- Diego
- Aris

## Descripción

Chat de texto desarrollado con Python y sockets TCP. Permite conectar varios clientes simultáneamente mediante hilos.

Los mensajes normales se envían a todos los demás usuarios conectados. También se pueden enviar mensajes privados con el comando `/msg`.

## Reto especial

Enviar un mensaje privado a un usuario específico sin que los demás usuarios conectados puedan recibirlo.

### Sintaxis

```text
/msg <usuario> <mensaje>
```

### Ejemplo

```text
/msg Diego Hola, este mensaje es privado
```

Diego recibirá:

```text
[privado de Aris] Hola, este mensaje es privado
```

Aris recibirá la confirmación:

```text
[privado para Diego] Hola, este mensaje es privado
```

Los demás usuarios no recibirán el mensaje.

## Requisitos

- Python 3.x
- Una terminal para el servidor
- Una terminal independiente para cada cliente

## Cómo ejecutar el proyecto

### 1. Iniciar el servidor

En la primera terminal:

```bash
python3 servidor.py
```

El servidor comenzará a escuchar conexiones en `localhost:5000`.

### 2. Iniciar los clientes

En una terminal independiente por cada usuario:

```bash
python3 cliente.py
```

Cada cliente deberá escribir un nombre de usuario único.

Para probar el proyecto se recomienda abrir al menos tres clientes.

## Comandos

### Mensaje público

Escribe cualquier mensaje normalmente:

```text
Hola a todos
```

El mensaje llegará a todos los usuarios, excepto al remitente.

### Mensaje privado

```text
/msg <usuario> <mensaje>
```

Ejemplo:

```text
/msg Lorenzo ¿Ya terminaste tu parte?
```

El mensaje solamente llegará a Lorenzo.

### Salir del chat

```text
/salir
```

También se puede utilizar:

```text
salir
```

## Manejo de errores

El proyecto controla las siguientes situaciones:

- Nombre de usuario vacío.
- Nombre de usuario repetido.
- Comando `/msg` incompleto.
- Destinatario no conectado.
- Desconexión normal con `/salir`.
- Desconexión abrupta de un cliente.
- Error al enviar un mensaje a un cliente desconectado.

Si un cliente se desconecta abruptamente, el servidor continúa funcionando para los demás usuarios.

## Archivos

- `servidor.py`: acepta conexiones, registra usuarios, procesa mensajes privados y realiza el broadcast.
- `cliente.py`: permite escribir mensajes y recibirlos simultáneamente.
- `README.md`: contiene las instrucciones y documentación del proyecto.

## Pruebas recomendadas

1. Conectar tres clientes con nombres diferentes.
2. Enviar un mensaje público.
3. Enviar un mensaje privado con `/msg`.
4. Intentar registrar un nombre repetido.
5. Enviar `/msg` sin destinatario o sin mensaje.
6. Enviar un mensaje a un usuario inexistente.
7. Salir normalmente con `/salir`.
8. Cerrar abruptamente un cliente y verificar que los demás continúan funcionando.