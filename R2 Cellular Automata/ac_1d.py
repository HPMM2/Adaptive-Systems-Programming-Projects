'''
 Universidad Autónoma de Nuevo León
 Fac. de Ingeniería Mecánica y Eléctrica
 Administración y Sistemas
 Ingeniería en Tecnologías de Software
 
 Programación de Sistemas Adaptativos
 Autómatas celulares
 Autómata con celdas binarias, donde cada celda tiene dos vecinos (1D)
'''

import sys

# Imprimir resultado con el formato establecido: 0=blanco, 1=*.
# Entrada: configuración
# Salida: configuración con formato (anexa guiones al principio y al final, 1 se sustituye por * y 0 por espacio)
def imprime_resultado(configuracion):
    resultado_formato='_'
    for celda in configuracion:
        if celda=='1':
            resultado_formato=resultado_formato + '*'
        else:
            resultado_formato=resultado_formato + ' '
    print(resultado_formato + "_")

# Aplicar la regla con la ventana recibida.
# Entrada: Ventana (coleccion de tres celdas, la central y dos vecinos a los lados)
# Salida: 0 o 1, dependiendo de la regla utilizada

# Regla 0: Cualquier cosa = 0
#def procesa_ventana(ventana):
#    return '0'

# Regla 51: Color contrario a la celda central, i.e. 0=1, 1=0
#def procesa_ventana(ventana):
#    if ventana[1]=='0':
#        resultado='1'
#    elif ventana[1]=='1':
#        resultado='0'
#    return resultado

# Regla 30: Caso por caso
#def procesa_ventana(ventana):
#    if ventana=='000' or ventana=='101' or ventana=='110' or ventana=='111': #Casos 0, 5, 6 y 7
#        return '0'
#    else: #Casos 001 (1), 010 (2), 011 (3) y 100 (4)
#        return '1'

# Regla 165: Vecinos con el mismo color=1, de otra manera=0    
#def procesa_ventana(ventana):
#    if ventana[0]==ventana[2]:
#        resultado='1'
#    else:
#        resultado='0'
#    return resultado


#Regla 17
def procesa_ventana(ventana):
    ventana_invertida = ventana[::-1]
    
    if ventana_invertida == '111' or ventana_invertida == '110' or ventana_invertida == '101' or ventana_invertida == '100':
        return '0'
    elif ventana_invertida == '011' or ventana_invertida == '010' or ventana_invertida == '001' or ventana_invertida == '000':
        return '1'


# Generar una nueva configuración de acuerdo a una regla (0-255)
# Entrada: configuración actual (t=i)
# Salida: configuración nueva (t=i+1)
def recorre_cadena(configuracion):
    nueva_configuracion=''

    for i in range(len(configuracion)):
        n=len(configuracion)
        ventana=configuracion[(i+(n-1))%n]+configuracion[i]+configuracion[(i+1)%n]
        nueva_configuracion=nueva_configuracion+procesa_ventana(ventana)
            
    return nueva_configuracion


#-------------------------------------------------------------
#Main (parte principal del programa)

# Cadenas de prueba
conf1="0000000000000000000000000000000000100000000000000000000000000000000000"
#conf2="0000100000"

configuracion_actual=conf1

# Toma la cantidad de iteraciones como argumento de la linea de comando
iteraciones=int(sys.argv[1])

# Por la cantidad fijada de iteraciones:
#   Imprime la cadena actual
#   Genera una nueva cadena de acuerdo a la regla
#   Reemplaza la cadena actual por esta nueva cadena
for i in range(iteraciones):
    imprime_resultado(configuracion_actual)
    nueva_configuracion=recorre_cadena(configuracion_actual)
    configuracion_actual=nueva_configuracion
