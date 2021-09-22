import socket
import threading
import time


def tcpLink(sock, addr, user):
    """
    多线程处理每一个客户端连接
    :param sock: 客户端socket
    :param addr: 客户端地址
    :param user: 用户字典
    :return:None
    """
    print('Accept new connection from {address}'.format(address=addr))
    sock.send("Welcome".encode('utf-8'))
    mode = sock.recv(10).decode('utf-8')  # 模式（login/submit）
    # 获取用户信息
    userName = sock.recv(16).decode('utf-8')
    userPassword = sock.recv(16).decode('utf-8')
    if mode == 'login':
        if userName in user:  # 校验用户信息
            if userPassword != user[userName]:
                sock.send('密码错误！'.encode('utf-8'))
                sock.send('0'.encode('utf-8'))
                sock.close()  # 关闭连接
                print('{address} Connection Denied.'.format(address=addr))
                print('Connection from addr {address} closed.'.format(address=addr))
                return
            sock.send('登录成功！'.encode('utf-8'))
            sock.send('1'.encode('utf-8'))
            print('{userName} Login'.format(userName=userName))
        else:
            sock.send('用户名不存在！'.encode('utf-8'))
            sock.send('0'.encode('utf-8'))
            sock.close()  # 关闭连接
            print('{address} Connection Denied.'.format(address=addr))
            print('Connection from addr {address} closed.'.format(address=addr))
            return
    else:
        sock.send('注册成功！'.encode('utf-8'))
        sock.send('1'.encode('utf-8'))
        print('{userName} Login'.format(userName=userName))
        user[userName] = userPassword  # 添加到用户字典
    # print('userName: {name}'.format(name=userName))
    # print('userPassword: {password}'.format(password=userPassword))

    # 接收用户消息
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('{name}: {msg}'.format(name=userName, msg=data.decode('utf-8')))

    sock.close()  # 关闭连接
    print('Connection from addr {address} closed.'.format(address=addr))


def server_TCP():
    """
    TCP服务器端主程序
    :return: None
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1234
    s.bind((host, port))

    s.listen(5)
    user = dict()
    print('等待连接...')
    while True:
        sock, addr = s.accept()
        # 每个连接创建一个线程
        t = threading.Thread(target=tcpLink, args=(sock, addr, user))
        t.start()
        print(user)


if __name__ == '__main__':
    server_TCP()
