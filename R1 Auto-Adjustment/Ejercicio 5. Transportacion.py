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


modos_terrenos = {
    "Terreno Plano": ["Transportación Normal", "Alas", "Formación de Estrella", "Ruedas de Tanque"],
    "Agua": ["Alas", "Formación de Estrella"],
    "Aire": ["Formación de Estrella","Alas"],
    "Terreno Sinuoso": ["Ruedas de Tanque", "Alas"],
    "Lava": ["Pies Anti-Derretimiento", "Alas"]
}

TIEMPO_ESPERA = 1
n = 31

for i in range(1, n + 1):
    terreno = random.choice(list(modos_terrenos.keys())) 
    modo = modos_terrenos[terreno]  
    modo = random.choice(modo) 
    
    print("Día:", i, "- Tipo de Terreno:", terreno, "    -  Modo:", modo)

    time.sleep(TIEMPO_ESPERA)
