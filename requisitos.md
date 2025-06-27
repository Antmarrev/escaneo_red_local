# Requisitos del Script de Escaneo de Red Local

## Objetivo
Desarrollar un script ligero en Python que escanee la red local, detecte dispositivos conectados y reporte los puertos abiertos por cada IP activa.

## Funcionalidades mínimas (MVP)
- Escaneo de subred local (ej: 192.168.1.0/24).
- Descubrimiento de IPs activas mediante ping.
- Escaneo de puertos comunes (ej: 22, 80, 443).
- Parámetros configurables: subred, lista de puertos, timeout.
- Resultados mostrados por consola de forma ordenada.
- Uso solo de librerías estándar de Python.

## Funcionalidades opcionales (futuras versiones)
- Guardar resultados en .json o .csv.
- Detección de nombre del host.
- Escaneo multihilo para mayor velocidad.
- Integración con herramientas como nmap.

## Fuera de alcance (por ahora)
- Escaneo fuera de la red local.
- Interfaz gráfica o web.
- Explotación de vulnerabilidades o técnicas ofensivas.
- Uso de librerías pesadas o no estándar (como scapy).
