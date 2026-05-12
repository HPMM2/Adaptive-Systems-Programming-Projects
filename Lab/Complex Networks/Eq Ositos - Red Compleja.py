# -*- coding: utf-8 -*-

import sys

#Función para leer un archivo
def leer_archivo(nombre_ar):
    try:
        archivo=open(nombre_ar)
        lineas=archivo.readlines()
        archivo.close()
    except IOError:
        print('No se pudo leer el archivo')
        sys.exit()
    return lineas



nombre_archivo="red_ositos.txt"

lineas=leer_archivo(nombre_archivo)

#Desplegar la cantidad de líneas del archivo (longitud de lista "lineas")
print()
print('Número de líneas: ',len(lineas))
print()

#Desplegamos el contenido de la lista "lineas"
print(lineas)
print()

#Desplegamos el contenido de cada elemento de la lista
for linea in lineas:
    print(linea)
