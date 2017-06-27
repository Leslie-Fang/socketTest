import socket
import time
HOST = "150.95.148.104"
PORT = 8070

while True:
    cmd1 = raw_input("Need to connect to the server Y or N:").strip()
    if cmd1 == 'Y':
        print("Try to connect")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Do connected")
        s.connect((HOST, PORT))
        cmd = raw_input("Please input msg:").strip()
        s.send(cmd)
        data = s.recv(1024)
        print data
        s.close()
    else:
        time.sleep(2)