import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 54321

s.sendto(str.encode("Hello", 'utf-8'), (host, port))
print(bytes.decode(s.recv(1024)))
s.close()
