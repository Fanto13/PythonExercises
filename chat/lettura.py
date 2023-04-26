import socket

HOST = '192.168.10.61'  # Indirizzo IP del server
PORT = 12000
# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Messaggio da inviare
while True:
    message = input("inserire un numero:")
    try:
        int(message)
    except:
        continue

    message = f"/n{message}"
    break

# Invia il messaggio al server
sock.sendto(message.encode(), (HOST, PORT))
data, addr = sock.recvfrom(1024)
print(data.decode())

# Chiude il socket
sock.close()