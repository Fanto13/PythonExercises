import socket
import threading

# creo il socket del client, gli passo l'indirizzo IP e la porta del server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# imposto l'indirizzo IP e la porta del server
HOST = "localhost"
PORT = 12345

# mi connetto al server
client_socket.connect((HOST, PORT))

# chiedo il nickname all'utente
nickname = input("Inserisci il tuo nickname: ")
client_socket.sendall(nickname.encode("utf-8"))

def receive_message():
    while True:
        # ricevo il messaggio dal server
        rcv_msg = client_socket.recv(1024).decode("utf-8")
        # stampo il messaggio
        print(rcv_msg)

# creo un thread per ricevere i messaggi dal server
t = threading.Thread(target=receive_message)
t.start()
print("scrivi il tuo messaggio, che sarà visualizzato dai partecipanti, per uscire scrivi /quit")
while True:
    # leggo l'input dall'utente
    msg = input()
    print (nickname, msg) # stampo il messaggio che sto inviando
    
    
    # controllo se l'utente ha inserito "/quit"
    if msg == "/quit":
        # invio il messaggio al server
        client_socket.sendall(msg.encode("utf-8"))
        # chiudo il socket del client
        client_socket.close()
        break
    
    # invio il messaggio al server
    client_socket.sendall(msg.encode("utf-8"))