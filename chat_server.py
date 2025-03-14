import socket
import threading
import configparser

def ler_config(arquivo):
    """Lê o host e a porta do arquivo de configuração"""
    config = configparser.ConfigParser()
    config.read(arquivo)
    host = config["DEFAULT"]["host"]
    port = int(config["DEFAULT"]["port"])
    return host, port

def handle_client(conn, addr):
    """Gerencia a comunicação com um cliente"""
    print(f"Conexão estabelecida com {addr}")
    
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"Cliente: {msg}")
            resposta = input("Servidor: ")
            conn.send(resposta.encode())
        except:
            break
    
    print(f"Conexão encerrada com {addr}")
    conn.close()

def main():
    host, port = ler_config("config.txt")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Servidor ouvindo em {host}:{port}...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "_main_":
    main()