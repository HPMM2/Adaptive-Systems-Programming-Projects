'''

Algunas funciones importantes:

 len(lista)
Devuelve la cantidad de elementos que tiene lista (si es lista anidada, serían los elementos del primer nivel).

 range(desde donde, hasta donde, cuanto avanzar)
Se utiliza junto con ciclos para determinar de que valor a que valor irá la variable del ciclo. Si solo usamos range(hasta dónde), se asume que se empieza desde cero y se avanza uno.

 sys.float_info.max [Usar libreria sys]
Regresa el numero más grande de punto flotante que utiliza Python

 pow(numero, potencia) [Usar librería math]
Eleva numero a la potencia indicada.

'''

from math import *
import sys

'''
  Entradas: puntoA y puntoB -- son listas numéricas de cualquier longitud (debe ser la misma longitud en ambas listas).
  Salida: Distancia euclidiana entre las listas.''' 
def calcularDistanciaEuclidiana(puntoA, puntoB):
    suma=0
    for i in range(len(puntoA)):
        suma=suma+pow(puntoA[i]-puntoB[i],2)
    return sqrt(suma)

#Datos. Contexto: colores
vectores=[[153,51,255],[121,236,221],[209,236,121],[240,164,76],[240,98,76],[76,93,240],[50,239,94]]
centroides=[[255,0,0],[0,255,0],[0,0,255]]

grupos=[]

#Asignación de grupos
for i in range(len(vectores)):
    distanciaMasCercana=sys.float_info.max
    centroideMasCercano=-1
    for j in range(len(centroides)):
        distancia=calcularDistanciaEuclidiana(vectores[i],centroides[j])
        if distancia<distanciaMasCercana:
            distanciaMasCercana=distancia
            centroideMasCercano=j
    grupos.append(centroideMasCercano)

print(grupos)

# Actualización de centroides
for j in range(len(centroides)):
    sumas = [0]*len(centroides[j])
    contador = 0
    for i in range(len(vectores)):
        if grupos[i] == j:
            for k in range(len(vectores[i])):
                sumas[k] += vectores[i][k]
            contador += 1
    if contador > 0:
        centroides[j] = [suma/contador for suma in sumas]

print(centroides)
from math import *
import sys

def calcularDistanciaEuclidiana(puntoA, puntoB):
    suma=0
    for i in range(len(puntoA)):
        suma=suma+pow(puntoA[i]-puntoB[i],2)
    return sqrt(suma)

vectores=[[153,51,255],[121,236,221],[209,236,121],[240,164,76],[240,98,76],[76,93,240],[50,239,94]]
centroides=[[255,0,0],[0,255,0],[0,0,255]]

grupos=[]

# Asignación de grupos
for i in range(len(vectores)):
    distanciaMasCercana=sys.float_info.max
    centroideMasCercano=-1
    for j in range(len(centroides)):
        distancia=calcularDistanciaEuclidiana(vectores[i],centroides[j])
        if distancia<distanciaMasCercana:
            distanciaMasCercana=distancia
            centroideMasCercano=j
    grupos.append(centroideMasCercano)

print(grupos)

# Actualización de centroides
for j in range(len(centroides)):
    sumas = [0]*len(centroides[j])
    contador = 0
    for i in range(len(vectores)):
        if grupos[i] == j:
            for k in range(len(vectores[i])):
                sumas[k] += vectores[i][k]
            contador += 1
    if contador > 0:
        centroides[j] = [suma/contador for suma in sumas]

print(centroides)










