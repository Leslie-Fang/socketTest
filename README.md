## 服务器端
    服务器的端的socket有两个，s是接受监听连接的socket
    conn是接受了连接之后新创建的socket，conn每次通信结束之后都需要销毁
    conn 是新创建的socket对象

    **非阻塞** socket的关键就是在阻塞socket的基础上将这个conn的socket放到一个子进程里面
    参考这个[链接](https://www.idaima.com/article/11725)
    当 socket 接受到（accept）一个请求，就 fork 出一个子进程 去处理这个请求。然后父进程继续接受请求。

## 客户端
    每一次通信创建一个socket，连接上服务器之后传输数据，然后通信结束之后需要close这个socket