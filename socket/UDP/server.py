import socket


def server_UDP():
    """
    UDP服务端程序
    :return:
    """
    # 设置socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 54321
    s.bind((host, port))
    print("Bind UDP on 54321...")

    user = dict()  # 设置用户字典
    while True:
        # 获得客户端发送的连接信息
        data, addr = s.recvfrom(1024)
        s.sendto(str.encode('发送成功', 'utf-8'), addr)
        print("received from: {address}".format(address=addr))
        print('{address}: {msg}'.format(address=addr, msg=data.decode()))
        mode, addr = s.recvfrom(10)  # 模式（login/submit）
        mode = mode.decode('utf-8')

        # 获取用户信息
        userName, addr = s.recvfrom(16)
        userName = userName.decode('utf-8')
        userPassword, addr = s.recvfrom(16)
        userPassword = userPassword.decode('utf-8')
        # 登录判断
        if mode == 'login':
            if userName in user:  # 校验用户信息
                if userPassword != user[userName]:
                    s.sendto('密码错误！'.encode('utf-8'), addr)
                    s.sendto('0'.encode('utf-8'), addr)
                    print('{address} Connection Denied.'.format(address=addr))
                    # s.close()
                    continue
                s.sendto('登录成功！'.encode('utf-8'), addr)
                s.sendto('1'.encode('utf-8'), addr)
                print('{userName} Login'.format(userName=userName))
            else:
                s.sendto('用户名不存在！'.encode('utf-8'), addr)
                s.sendto('0'.encode('utf-8'), addr)
                print('{address} Connection Denied.'.format(address=addr))
                # s.close()
                continue
        else:
            s.sendto('注册成功！'.encode('utf-8'), addr)
            s.sendto('1'.encode('utf-8'), addr)
            print('{userName} Login'.format(userName=userName))
            user[userName] = userPassword  # 添加到用户字典

        # 获得客户端发送的消息并显示
        while True:
            data, addr = s.recvfrom(1024)
            if not data or data.decode('utf-8') == 'exit':
                break
            print('{name}: {msg}'.format(name=userName, msg=data.decode('utf-8')))
        print('{name} Logout'.format(name=userName))

    s.close()  # 关闭连接


if __name__ == '__main__':
    server_UDP()
