import socket
import time
HOST = "47.91.245.251"
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
    #simulate the block status
    time.sleep(30)
    conn.send("server received you message.")
    #when communicate with one client need to close the socket
    conn.close()
s.close()
