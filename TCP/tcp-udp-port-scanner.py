import socket

ip = input("Enter IP: ")

for port in range(1,  65535):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp socket
    scanner.settimeout(1)

    try:
        scanner.connect((ip, port))
        print(f"Port {port} is OPEN")

    except Exception as e:
        print(f"port {port}: {e}")
        

    scanner.close()
