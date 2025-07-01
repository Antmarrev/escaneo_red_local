"""
Script de escaneo de red local

Este script permite detectar qué dispositivos están activos en una red local (por ejemplo, 192.168.1.0/24)
y qué puertos tienen abiertos. Es una herramienta básica de reconocimiento útil para tareas de
administración de sistemas o ciberseguridad.

¿Qué hace?
- Escanea IPs dentro de una subred y comprueba cuáles están activas.
- Por cada IP activa, intenta conectar a varios puertos conocidos (como 22, 80, 443).
- Muestra los resultados por consola.

¿Para qué sirve?
- Para identificar dispositivos conectados a una red.
- Para conocer qué servicios están expuestos (puertos abiertos).
- Para realizar una primera fase de reconocimiento en una auditoría de seguridad.

Autor: Antonio Martín (proyecto personal)
Fecha de inicio: 23 de junio de 2025
"""
import socket
import ipaddress
import subprocess
import platform
import time

subred_objetivo = "..." #subred del usuario
puertos_a_escanear = [] 
timeout_conexion = 0.5 #tiempo máximo de espera en segundos

def generar_ips(subred):
    """
    Genera todas las direcciones IP de una subred dada.
    
    Args:
        subred (str): Subred en formato CIDR, por ejemplo '192.168.1.0/24'.
    
    Returns:
        list: Lista de direcciones IP como strings.
    """
    try:
        red = ipaddress.ip_network(subred, strict=False)
        lista_ips = [str(ip) for ip in red.hosts()]  # hosts() excluye la IP de red y broadcast
        return lista_ips
    except ValueError as e:
        print(f"Error en la subred proporcionada: {e}")
        return []

def ping_host(ip):
    """
    Realiza un ping a una dirección IP para comprobar si está activa.
    
    Args:
        ip (str): Dirección IP a la que hacer ping.
    
    Returns:
        bool: True si la IP responde, False si no.
    """
    sistema = platform.system() #detecta el sistema operativo

    if sistema == "Windows":
        comando = ["ping", "-n", "1", "-w", "1000", ip]
    else: #Linux
        comando = ["ping", "-c", "1", "-W", "1", ip]

    try:
        resultado = subprocess.run(
            comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return resultado.returncode == 0
    except Exception as e:
        print(f"Error al hacer ping a {ip}: {e}")
        return False


def escanear_puertos(ip, lista_puertos):
    """
    Escanea una lista de puertos en una dirección IP y devuelve los puertos abiertos.
    
    Args:
        ip (str): Dirección IP a escanear.
        lista_puertos (list): Lista de puertos a escanear.
    
    Returns:
        list: Lista de puertos abiertos en la IP.
    """
    puertos_abiertos = []

    for puerto in lista_puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout_conexion)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            puertos_abiertos.append(puerto)
        sock.close()

    return puertos_abiertos


def mostrar_resultados(resultados):
    """
    Muestra los resultados del escaneo de red de forma ordenada.
    
    Args:
        resultados (dict): Diccionario con IPs como claves y listas de puertos abiertos como valores.
    """
    for ip, puertos in resultados.items():
        if puertos:
            print(f"{ip} - puertos abiertos: {puertos}")
        else:
            print(f"{ip} - sin puertos abiertos detectados")

if __name__ == "__main__":
    """
    Bloque principal de ejecución del script de escaneo de red local.
    """

    subred_objetivo = input("Introduce la subred a escanear (ejemplo 192.168.1.0/24): ").strip()
    puertos_input = input("Introduce los puertos a escanear separados por comas (ejemplo 22,80,443): ").strip()
    puertos_a_escanear = [int(p.strip()) for p in puertos_input.split(",") if p.strip().isdigit()]

    lista_ips = generar_ips(subred_objetivo)
    print(f"Escaneando puertos en dispositivos activos en {subred_objetivo}...\n")
    resultados = {}

    for ip in lista_ips:
        if ping_host(ip):
            print(f"{ip} está activa, escaneando puertos...")
            puertos_abiertos = escanear_puertos(ip, puertos_a_escanear)
            resultados[ip] = puertos_abiertos

    print("\nResultados del escaneo:")
    mostrar_resultados(resultados)