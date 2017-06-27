import socket

HOST = "150.95.148.104"
PORT = 8070
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    conn, addr = s.accept()
    print 'Connected by ', addr
    data = conn.recv(1024)
    print data
    conn.send("server received you message.")
   # while True:
   #     data = conn.recv(1024)
   #     print data
   #     conn.send("server received you message.")