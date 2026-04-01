import socket
import threading
import os

LOG_FILE = "logs/attacks.log"
os.makedirs("logs", exist_ok=True)

def handle_client(client_socket, addr):
    print(f"[+] Connection from {addr}")
    client_socket.send(b"SSH-2.0-OpenSSH_7.4\r\n")

    try:
        data = client_socket.recv(1024)
        log = f"{addr[0]} -> {data.decode(errors='ignore')}\n"

        print("[ATTACK]", log)

        with open(LOG_FILE, "a") as f:
            f.write(log)

        client_socket.send(b"Permission denied\n")
    except:
        pass

    client_socket.close()

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 2222))
    server.listen(5)

    print("[*] Fake SSH Honeypot running on port 2222")

    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()

if __name__ == "__main__":
    start()