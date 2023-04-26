import socket
UDP_IP = "192.168.10.61"  # Replace with the IP address of the destination
UDP_PORT = 12000       # Replace with the port number of the destination

message = input("Inserire un messaggio: ")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the message
sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

# Close the socket
sock.close()