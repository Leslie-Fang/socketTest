import socket
import time
import os
HOST = "150.95.148.104"
PORT = 8070
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    #服务器的端的socket有两个，s是接受监听连接的socket
    #conn是接受了连接之后新创建的socket，conn每次通信结束之后都需要销毁
    #conn 是新创建的socket对象
    conn, addr = s.accept()
    pid = os.fork()
    #pid =0 ,children process
    if pid == 0:
        #need to close s socket in the children process
        s.close()
        print 'Connected by ', addr
        data = conn.recv(1024)
        print data
        #simulate the block status
        time.sleep(30)
        conn.send("server received you message.")
        #when communicate with one client need to close the socket
        conn.close()
        #exit the chridren
        os._exit(0)
    else:
        #in the father process
        #just close the conn socket
        #then go loop for listen again
        conn.close()
s.close()
