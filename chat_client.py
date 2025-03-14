import socket
import sys
import configparser

def ler_config(arquivo):
    """Lê o host e a porta do arquivo de configuração"""
    config = configparser.ConfigParser()
    config.read(arquivo)
    host = config["DEFAULT"]["host"]
    port = int(config["DEFAULT"]["port"])
    return host, port

def main():
    host, port = ler_config("config.txt")
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    print("Conectado ao servidor! Digite suas mensagens:")

    while True:
        if len(sys.argv) > 1:
            mensagem = " ".join(sys.argv[1:])
        else:
            mensagem = input("Cliente: ")
        
        if mensagem.lower() == "sair":
            break
        
        client.send(mensagem.encode())
        resposta = client.recv(1024).decode()
        print(f"Servidor: {resposta}")

    client.close()

if __name__ == "_main_":
    main()