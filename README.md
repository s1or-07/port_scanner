
### Liberia sys - System-specific parameters and functions

La biblioteca `sys` en Python es una biblioteca estándar que proporciona funciones y variables utilizadas para manipular diferentes partes del entorno de ejecución de Python.

Básicamente nos permite solicitar ya sea una dirección IP o el nombre del host, para ser mas especifico, de esta librería requerimos el parámetro para argumentos

```python
import sys
```
### Liberia socket - Low-level networking interface

La biblioteca `socket` en Python es una parte esencial de la biblioteca estándar que proporciona una interfaz para el acceso a la funcionalidad de red de bajo nivel. Esta biblioteca permite la creación de aplicaciones de red que pueden comunicarse entre sí a través de protocolos como TCP y UDP

Básicamente nos sirve para poder trabajar con redes, nos permite crear una conexión con los puertos de una maquina, es decir interactuar con la red.

```python
import socket
```

### Code

1. **Primero, verificamos el numero de argumentos de la línea de comandos**

```python
if len(sys.argv) == 2:
```

`len(sys.argv) == 2` Verifica si se ha pasado exactamente un argumento (además del nombre del script). Si no hay argumentos o hay más de uno, la condición será falsa.

`sys.argv` es una lista en Python que contiene los argumentos de línea de comandos pasados al script. `sys.argv[0]` es el nombre del script, y `sys.argv[1]` es el primer argumento pasado al script.

2. **Luego, convertimos el nombre del host a una dirección IP**

```python
target = socket.gethostbyname(sys.argv[1])
```

`socket.gethostbyname(sys.argv[1])` toma el primer argumento de la línea de comandos (presumiblemente un nombre de host) y lo convierte en una dirección IP.

Asignamos la dirección IP resultante a la variable `target`.

3. **Manejo de errores**

```python
else:
	print("Ingrese el host")
	exit()
```

Si no se proporciona exactamente un argumento, el programa imprime "Ingrese el host".

`exit()` termina la ejecución del programa.

4. **Definimos una función para poder obtener el servicio de los puertos a la hora de escanearlos**

```python
def get_port_service(port):
	try:
		service = socket.getservbyport(port)
	except:
		service = "Desconocido"
	return service
```

- `def` es la palabra clave en Python que se utiliza para definir una función.
- `get_port_service` es el nombre de la función.
- `port` es el parámetro de la función, que representa el número de puerto para el cual queremos determinar el nombre del servicio.

**Bloque Try-Except**

- `try:` inicia un bloque de código que intentará ejecutarse.
- `service = socket.getservbyport(port)` usa la función `getservbyport` del módulo `socket` para obtener el nombre del servicio asociado con el número de puerto proporcionado. Por ejemplo, si el puerto es 80, esta función devolverá "http".
- `socket.getservbyport(port)` puede lanzar una excepción si no se puede encontrar un servicio asociado con el puerto dado.
- `except:` captura cualquier excepción que ocurra en el bloque `try`.
- `service = "Desconocido"` establece la variable `service` a "Desconocido" si ocurre una excepción, lo que significa que no se pudo determinar el nombre del servicio para ese puerto.

**Return service**

`return service` devuelve el nombre del servicio encontrado o "Desconocido" si ocurrió una excepción.

5. **Escáner**

**Bucle**

```python
for port in range(1,6535):
```

`for port in range(1, 65535):` itera sobre todos los puertos del 1 al 65534. El rango en Python es inclusivo en el inicio e inclusivo en el final menos uno.

**Creación de socket**

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` crea un nuevo socket.
- `socket.AF_INET` especifica que se está utilizando el protocolo IPv4.
- `socket.SOCK_STREAM` especifica que se está utilizando el protocolo TCP.

**Tiempo de espera**

```python
socket.setdefaulttimeout(1)
```

Este establece el tiempo de espera para las conexiones en 1 segundo. Esto significa que si el intento de conexión no tiene éxito en 1 segundo, se considera fallido.

**Intento de conexión**

```python
result = s.connect_ex((target,port))
```

- `result = s.connect_ex((target, port))` intenta conectarse al puerto `port` en el objetivo `target`. `connect_ex` devuelve un código de error en lugar de lanzar una excepción.
- Si la conexión tiene éxito, `connect_ex` devuelve 0.
- Si la conexión falla, devuelve un código de error distinto de 0.

```python
if result = 0
```

`if result == 0:` verifica si la conexión fue exitosa (es decir, si el puerto está abierto).

**Obtener el puerto y su servicio y mostrar el resultado**

```python
service = get_port_service(port)
print("{}/tcp\tOPEN\t{}".format(port,service))

s.close()
```

- `service = get_port_service(port)` obtiene el nombre del servicio asociado con el puerto utilizando la función `get_port_service`.
- `print("El Puerto {} está abierto".format(port,service))` imprime que el puerto está abierto y muestra el nombre del servicio si está disponible. Sin embargo, hay un pequeño error en el `print` que intentaré corregir más adelante.
- `s.close()` cierra el socket para liberar los recursos asociados con él.