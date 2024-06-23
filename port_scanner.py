import sys
import socket
#from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Ingrese el target")
    exit()

def get_port_service(port):
    try:
        service = socket.getservbyport(port)
    except:
        service = "Desconocido"
    return service

print("-" * 35)
print("Ip del target: " + target)
print("-" * 35)

try:
    print("PORT\tESTADO\tSERVICIO")
    print("-" * 30)
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            service = get_port_service(port)
            print("{}/tcp\tOPEN\t{}".format(port,service))
        s.close()

except KeyboardInterrupt:
    print("-" * 27)
    print("\nAnalisis Finalizado")
    sys.exit()

except socket.gaierror:
    print("La resolucion del host ha fallado")
    sys.exit()

except socket.error:
    print("El host no responde")
    sys.exit()
