'''
 Universidad Autónoma de Nuevo León
 Fac. de Ingeniería Mecánica y Eléctrica
 Administración y Sistemas
 Ingeniería en Tecnologías de Software
 
 Programación de Sistemas Adaptativos
 Auto-ajuste
 Simulación donde se ajusta el estado de un foco centinela
'''

import time
import random

def trapezoidal(x,a,b,c,d):
    if a<=x and x<=b:
        return (x-a)/(b-a)
    elif b<=x and x<=c:
        return 1
    elif c<=x and x<=d:
        return (d-x)/(d-c)
    else:
        return 0

def obtener_percepcion(hora):
   
    #FORMA 1: Diccionario
    #mapeo_hora_luz={0:0,1:0,2:0,3:0,4:0,5:0.3,6:0.3,7:0.5,8:0.5,9:0.7,10:0.7,11:0.7,12:1,13:1,14:1,15:0.1,16:0.7,17:0.7,18:0.7,19:0.5,20:0.5,21:0,22:0,23:0}
    #return mapeo_hora_luz[hora]
    
    #FORMA 2: Función trapezoidal
    percepcion=trapezoidal(hora,5,12,15,21)
    return percepcion


def realizar_ajuste(percepcion):
    #FORMA 1: Reglas
    '''if percepcion<0.5:
        return "Foco centinela PRENDIDO"
    else:
        return "Foco centinela APAGADO"'''
    
    #FORMA 2: Expresión matemática
    estado=1-percepcion
    return "Intensidad del foco: "+str(round(estado,3))

TIEMPO_ESPERA=1

for i in range(24):
    luz=obtener_percepcion(i)
    estado_foco=realizar_ajuste(luz)
    
    print("Hora: ",i," Luz: ",round(luz,3)," -- ",estado_foco)
    
    time.sleep(TIEMPO_ESPERA)