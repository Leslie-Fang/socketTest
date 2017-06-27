import socket
import time
HOST = "150.95.148.104"
PORT = 8070

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    cmd1 = raw_input("Need to connect to the server Y or N:").strip()
    if cmd1 == 'Y':
        s.connect((HOST, PORT))
        cmd = raw_input("Please input msg:").strip()
        s.send(cmd)
        data = s.recv(1024)
        print data
        s.close()
    else:
        time.sleep(2)