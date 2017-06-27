import socket

HOST = "150.95.148.104"
PORT = 8070

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = raw_input("Please input msg:").strip()
    s.send(cmd)
    data = s.recv(1024)
    print data