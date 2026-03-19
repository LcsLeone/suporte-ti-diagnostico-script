import os
import platform
import psutil
import socket

def info_sistema():
    print("=== INFORMAÇÕES DO SISTEMA ===")
    print(f"Sistema: {platform.system()}")
    print(f"Versão: {platform.version()}")
    print(f"Processador: {platform.processor()}")

def uso_sistema():
    print("\n=== USO DO SISTEMA ===")
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"Memória: {psutil.virtual_memory().percent}%")

def teste_internet():
    print("\n=== TESTE DE INTERNET ===")
    try:
        socket.create_connection(("8.8.8.8", 53))
        print("Internet: OK")
    except:
        print("Sem conexão com a internet")

def main():
    print("🔧 DIAGNÓSTICO RÁPIDO - SUPORTE TI\n")
    info_sistema()
    uso_sistema()
    teste_internet()

if __name__ == "__main__":
    main()