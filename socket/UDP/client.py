import socket


def client():
    """
    UDP客户端程序
    :return:None
    """
    # 设置socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 54321
    # 发送验证信息
    s.sendto(str.encode("Hello", 'utf-8'), (host, port))
    print(bytes.decode(s.recv(1024)))

    # 输入用户名、密码并选择模式
    name = input("请输入用户名：")
    password = input("请输入密码：")
    print('请选择模式（1登录    2注册）')
    mode = input()

    # 判断是否登录成功
    if mode == '1':
        s.sendto('login'.encode('utf-8'), (host, port))
    else:
        s.sendto('submit'.encode('utf-8'), (host, port))
    # 向server发送相应数据
    s.sendto(name.encode('utf-8'), (host, port))
    s.sendto(password.encode('utf-8'), (host, port))

    # 得到返回信息
    print(s.recv(1024).decode('utf-8'))
    isConnect = s.recv(10).decode('utf-8')

    # 若连接成功则继续发送消息
    if isConnect == '1':
        message = input()
        while message != 'exit':  # 用户输入exit则退出连接
            s.sendto(message.encode('utf-8'), (host, port))
            message = input()
        s.sendto(message.encode('utf-8'), (host, port))
    s.close()


if __name__ == '__main__':
    client()
