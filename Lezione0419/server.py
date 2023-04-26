import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 12000

server_socket = socket.socket( # qui creo il socket 
    socket.AF_INET, socket.SOCK_DGRAM #AF_INET è l'indirizzo IP, SOCK_DGRAM è il protocollo UDP e li definisce come socket
)  # nella libreria socket, chiami l'oggetto socket
server_socket.bind(#il bind serve per mettersi in ascolto su un indirizzo IP e una porta
    (UDP_IP_ADDRESS, UDP_PORT_NO)
)  

print("UDP server up and listening")

# preparazione all'applicazione
contatore = 0


# sviluppo l'applicazione, la funzione app riceve il messaggio e restituisce la risposta
def app(msg):
    if msg[0:2] != "/n":#tra il primo e il secondo carattere deve esserci /n
        return f"Protocollo errato"
    else:
        msg = msg[2:]#elimino i primi due caratteri
        try:
            numero = int(msg)#trasformo il messaggio in un numero intero, così da prevenire errori lato client
            contatore += numero
            return f"Siamo al numero: {contatore}"
        except:
            return f"Accetto solo numeri interi!"


while True:
    data, addr = server_socket.recvfrom(1024)  #recvfrom è un metodo che riceve i dati dall'indirizzo IP e dalla porta
    print(
        "Received message: ", addr, data.decode() #stampo a video l'indirizzo e i dati decodificati
    )  # stampo a video l'indirizzo e i dati decodificati
    msg = data.decode()  # messaggio testuale

    if addr[0] == UDP_IP_ADDRESS and data.decode() == "quit":
        print("sto chiudendo il server...")
        break

    resp = app(msg)

    server_socket.sendto(resp.encode(), addr)


print("server chiuso")
