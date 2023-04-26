import socket
UDP_IP_ADDRESS = "192.168.10.61"
UDP_PORT_NO = 12000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_STREAM
server_socket.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("UDP server up and listening")

# preparazione all'applicazione
contatore = 0
utenti = {}
# sviluppo l'applicazione
def app(addr, msg):
    global utenti
    
    command = msg[0:2]
    payload  = msg[2:]
    #registrare l'utente
    if command == "/r":
        utenti[payload] = addr #questo è un dizionario che ha come chiave il nome dell'utente e come valore l'indirizzo
    #leggere il messaggio e inoltrarlo
    elif command == "/m":
        addr = utenti[utenti]
    #leggere solo se non va in porto prima
    elif command == "/l":
        pass
    #sloggare
    elif command == "/e":
        pass
    
    else:
        msg = msg[2:]

    # numero = int(msg)
    try:
        numero = int(msg)
    except:
        return "Accetto solo numeri!"
    
    contatore += numero
    return f"Siamo al numero: {contatore}"

while True:
    data, addr = server_socket.recvfrom(1024)
    print("Received message:", addr, data.decode())
    msg = data.decode()
    if (addr[0] == "192.168.10.202" or addr[0] == "192.168.10.61") and data.decode() == "quit":
        break

    resp = app(addr, msg)

    server_socket.sendto(resp.encode(), addr)