# Pseudocódigo del Script de Escaneo de Red Local

## Objetivo de esta etapa
Diseñar la lógica básica del script en un formato comprensible y estructurado antes de escribir el código real en Python.

## Pseudocódigo

Inicio del programa

1. Pedir al usuario o definir por defecto:
   - Subred objetivo (ej: 192.168.1.0/24)
   - Lista de puertos a escanear (ej: [22, 80, 443])
   - Timeout por intento (ej: 0.5 segundos)

2. Generar todas las IPs posibles en la subred

3. Para cada IP en la subred:
   - Hacer ping para ver si está activa
   - Si responde:
       - Añadir a la lista de IPs activas

4. Para cada IP activa:
   - Para cada puerto de la lista:
       - Intentar abrir conexión (usando socket)
       - Si la conexión es exitosa:
           - Guardar el puerto como abierto

5. Mostrar por pantalla los resultados:
   - Para cada IP activa:
       - Mostrar qué puertos están abiertos

Fin del programa
