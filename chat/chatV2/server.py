import socket
import threading

# creo il socket del server
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# imposto l'indirizzo IP e la porta del server
HOST = "localhost"
PORT = 12345

# collego il socket all'indirizzo e alla porta
serv_socket.bind((HOST, PORT))

# definisco una funzione che gestisce la connessione con un client
def handle_client(client_socket, nickname):
    # stampo il nickname del cliente appena connesso
    print(f"{nickname} si è connesso.")
    
    while True:
        # ricevo il messaggio dal client
        rcv_msg = client_socket.recv(1024).decode("utf-8")
        
        # controllo se il messaggio è "/quit"
        if rcv_msg == "/quit":
            # stampo che il client si è disconnesso
            print(f"{nickname} si è disconnesso.")
            break
        
        # stampo il messaggio del client
        print(f"{nickname}: {rcv_msg}")
        
        # invio il messaggio a tutti i client tranne a quello che l'ha inviato
        for c in clients:
            if c[1] != nickname:
                c[0].sendall(f"{nickname}: {rcv_msg}".encode("utf-8"))

    # chiudo la connessione con il client
    client_socket.close()
    # rimuovo il client dalla lista
    clients.remove((client_socket, nickname))
    # invio un messaggio a tutti i client per avvertirli che il client si è disconnesso
    for c in clients:
        c[0].sendall(f"{nickname} si è disconnesso".encode("utf-8"))

# inizializzo la lista dei client connessi
clients = []

# avvio il server
print("Server avviato!")
serv_socket.listen()

while True:
    # accetto una connessione dal client
    client_socket, address = serv_socket.accept()
    
    # ricevo il nickname dal client
    nickname = client_socket.recv(1024).decode("utf-8")
    
    # aggiungo il client alla lista dei client connessi
    clients.append((client_socket, nickname))
    
    # creo un thread per gestire la connessione con il client
    t = threading.Thread(target=handle_client, args=(client_socket, nickname))
    t.start()