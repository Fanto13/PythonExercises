import socket

UDP_IP_ADDRESS = '192.168.10.61'  # Indirizzo IP locale
UDP_PORT_NO = 12000         # Porta su cui ascoltare

# Crea un socket UDP
server_socket = socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("udp up and listening")

contatore = 0
def app(msg):
    global contatore:
    try:
        numero = int(msg)
    except:
        contatore += numero
    return "accetto solo numeri!"
    return msg
    
while True:
    # Riceve il messaggio e l'indirizzo del client
    data, addr = server_socket.recvfrom(1024)
    print("received message:", addr, data.decode())
    msg=data.decode()
    
   
    
    resp = app(msg)
