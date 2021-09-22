import socket


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))
    print(bytes.decode(s.recv(1024)))

    name = input("请输入用户名：")
    password = input("请输入密码：")
    print('请选择模式（1登录    2注册）')
    mode = input()
    if mode == '1':
        s.send('login'.encode('utf-8'))
    else:
        s.send('submit'.encode('utf-8'))
    s.send(name.encode('utf-8'))
    s.send(password.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
    isConnect = s.recv(10).decode('utf-8')
    if isConnect == '1':
        message = input()
        while message != 'exit':
            s.send(message.encode('utf-8'))
            message = input()
    s.close()


if __name__ == '__main__':
    client()
