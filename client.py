import socket

def client_start(host, port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def senden(socket_obj, nachricht):
    socket_obj.sendall(nachricht.encode())
    print("gesendet")

def empfangen(socket_obj):
    data = socket_obj.recv(1024).decode()
    print(f"Empfangen: {data}")

if __name__ == "__main__":
    s = client_start("spielwiese.local", 5000)  # Server-IP
    while True:
        empfangen(s)
        senden(s, input())
