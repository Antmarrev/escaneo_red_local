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

subred_objetivo = "192.168.1.38/24" #subred del usuario
puertos_a_escanear = [22, 80, 443, 3389] #puertos más comunes, se podría optimizar para escanear todos los puertos
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
        comando = ["ping", "-n", "1", "-W", "1000", ip]
    else: #Linux o Mac
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
    pass

def mostrar_resultados(resultados):
    """
    Muestra los resultados del escaneo de red de forma ordenada.
    
    Args:
        resultados (dict): Diccionario con IPs como claves y listas de puertos abiertos como valores.
    """
    pass

if __name__ == "__main__":
    """
    Bloque principal de ejecución del script de escaneo de red local.
    """
    lista_ips = generar_ips(subred_objetivo)
    print(f"IPs activas en {subred_objetivo}:")
    for ip in lista_ips:
        if ping_host(ip):
            print(f"{ip} está activa")
    # Generar lista de IPs de la subred
    # TODO: llamar a generar_ips(SUBRED_OBJETIVO)

    # Comprobar qué IPs están activas
    # TODO: llamar a ping_host(ip) para cada IP generada

    # Escanear puertos de las IPs activas
    # TODO: llamar a escanear_puertos(ip, PUERTOS_A_ESCANEAR)

    # Mostrar resultados
    # TODO: llamar a mostrar_resultados(resultados)
