# Script de Escaneo de Red Local 🕵️‍♂️💻

## Descripción

Este script en Python permite realizar un escaneo básico de una red local (LAN), identificando qué dispositivos están conectados y qué puertos tienen abiertos. Es una herramienta útil como primer paso en tareas de ciberseguridad, administración de sistemas o simplemente para aprender cómo funciona una red.

## ¿Qué hace el script?

- Escanea una subred (ej. `192.168.1.0/24`) buscando dispositivos activos.
- Usa ping para detectar hosts vivos.
- Escanea puertos comunes (como 22, 80, 443) en cada IP activa.
- Muestra los resultados en consola de forma clara.

## ¿Para qué sirve?

- Para descubrir dispositivos conectados a tu red (incluyendo posibles intrusos).
- Para conocer qué servicios están expuestos en tu red (puertos abiertos).
- Como parte de un proceso de auditoría o diagnóstico de red.

## Requisitos

- Python 3.x
- Sistema operativo con soporte para comandos de red (funciona en Windows, Linux y macOS).
- No requiere instalar librerías externas.

## Ejemplo de uso

Ejecuta el script desde la terminal con:

python script.py

El script te pedirá:

-La subred a escanear:
    Por ejemplo:
    Introduce la subred a escanear (ejemplo 192.168.1.0/24): 192.168.1.0/24

-Los puertos a escanear separados por comas:
    Por ejemplo:
    Introduce los puertos a escanear separados por comas (ejemplo 22,80,443): 22,80,443

A continuación, el script mostrará en consola las IPs activas detectadas en tu red local y qué puertos están abiertos en cada una, de forma clara y ordenada.


## Estado del proyecto

✅ Documentación de requisitos  
✅ Diseño lógico en pseudocódigo  
✅ Desarrollo del script completado  
✅ Pruebas realizadas con éxito  
✅ Listo para usar en entornos de práctica

## Autor

Antonio Martín  
Junio 2025
