import socket


def server_UDP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 54321
    s.bind((host, port))

    print("Bind UDP on 54321...")
    while True:
        data, addr = s.recvfrom(1024)
        print("received from: %s:%s." % addr)
        print(data.decode())
        s.sendto(str.encode('发送成功', 'utf-8'), addr)
    s.close()


if __name__ == '__main__':
    server_UDP()
