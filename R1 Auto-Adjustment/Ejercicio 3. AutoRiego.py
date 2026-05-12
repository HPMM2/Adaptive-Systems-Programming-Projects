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



def humedad_suelo():
    return random.randint(0, 100)

def temperatura_promedio():
    return random.randint(20, 40)



TIEMPO_ESPERA=1
n=31
for i in range(1, n+1):
    humedad = humedad_suelo()
    temperatura = temperatura_promedio()
    
    print("Día: ",i," Temperatura promedio - ",temperatura,"°C, Humedad - ",humedad,"%")
    
    time.sleep(TIEMPO_ESPERA)