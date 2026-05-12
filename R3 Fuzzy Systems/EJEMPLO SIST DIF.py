import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

dano=ctrl.Antecedent(np.arange(0,101,1),'dano')
intensidad=ctrl.Antecedent(np.arange(0,101,1),'intensidad')
velocidad=ctrl.Consequent(np.arange(0,101,1),'velocidad')

#Daño
dano['ileso'] = fuzz.trapmf(dano.universe, [0, 0, 5, 10])
dano['menor'] = fuzz.trapmf(dano.universe, [5, 15, 20, 30])
dano['serio'] = fuzz.trapmf(dano.universe, [25, 30, 50, 75])
dano['critico'] = fuzz.trapmf(dano.universe, [70, 90, 100, 100])

dano.view()

#Intensidad
intensidad['leve'] = fuzz.trapmf(intensidad.universe, [0, 0, 10, 30])
intensidad['imoderada'] = fuzz.trapmf(intensidad.universe, [20, 30, 60, 70])
intensidad['fuerte'] = fuzz.trapmf(intensidad.universe, [60, 80, 100, 100])

intensidad.view()

#Velocidad
velocidad['lenta'] = fuzz.trapmf(velocidad.universe, [0, 0, 5, 20])
velocidad['moderada'] = fuzz.trapmf(velocidad.universe, [10, 30, 60, 70])
velocidad['rapida'] = fuzz.trapmf(velocidad.universe, [60, 90, 100, 100])

velocidad.view()
rule1 = ctrl.Rule(dano['ileso'] & intensidad['leve'], velocidad['lenta'])
rule2 = ctrl.Rule(dano['menor'] & intensidad['leve'], velocidad['moderada'])
rule3 = ctrl.Rule(dano['serio'] & intensidad['leve'], velocidad['lenta'])
rule4 = ctrl.Rule(dano['critico'] & intensidad['leve'], velocidad['lenta'])

rule5 = ctrl.Rule(dano['ileso'] & intensidad['imoderada'], velocidad['moderada'])
rule6 = ctrl.Rule(dano['menor'] & intensidad['imoderada'], velocidad['rapida'])
rule7 = ctrl.Rule(dano['serio'] & intensidad['imoderada'], velocidad['moderada'])
rule8 = ctrl.Rule(dano['critico'] & intensidad['imoderada'], velocidad['lenta'])

rule9 = ctrl.Rule(dano['ileso'] & intensidad['fuerte'], velocidad['rapida'])
rule10 = ctrl.Rule(dano['menor'] & intensidad['fuerte'], velocidad['rapida'])
rule11 = ctrl.Rule(dano['serio'] & intensidad['fuerte'], velocidad['moderada'])
rule12 = ctrl.Rule(dano['critico'] & intensidad['fuerte'], velocidad['lenta'])

rules=[]
rules.append(rule1)
rules.append(rule2)
rules.append(rule3)
rules.append(rule4)
rules.append(rule5)
rules.append(rule6)
rules.append(rule7)
rules.append(rule8)
rules.append(rule9)
rules.append(rule10)
rules.append(rule11)
rules.append(rule12)

sistema = ctrl.ControlSystem(rules)

caso=ctrl.ControlSystemSimulation(sistema)

#Entradas nítidas
caso.input['dano'] = 7
caso.input['intensidad'] = 65

# Calcular salida
caso.compute()
caso.output['velocidad']

velocidad.view(sim=caso)

x = np.arange(0, 101, 1)
mfx = fuzz.trapmf(x, [10, 30, 60, 70])
defuzz_centroid = fuzz.defuzz(x, mfx, 'centroid')  # Same as skfuzzy.centroid
defuzz_bisector = fuzz.defuzz(x, mfx, 'bisector')
defuzz_mom = fuzz.defuzz(x, mfx, 'mom')
defuzz_som = fuzz.defuzz(x, mfx, 'som')
defuzz_lom = fuzz.defuzz(x, mfx, 'lom')
xvals = [defuzz_mom,
         defuzz_som,
         defuzz_lom]
ymax = [fuzz.interp_membership(x, mfx, i) for i in xvals]

import matplotlib.pyplot as plt

labels = ['centroid', 'bisector', 'mean of maximum', 'min of maximum',
          'max of maximum']
xvals = [defuzz_centroid,
         defuzz_bisector,
         defuzz_mom,
         defuzz_som,
         defuzz_lom]
colors = ['r', 'b', 'g', 'c', 'm']
ymax = [fuzz.interp_membership(x, mfx, i) for i in xvals]

# Display and compare defuzzification results against membership function
plt.figure(figsize=(8, 5))

plt.plot(x, mfx, 'k')
for xv, y, label, color in zip(xvals, ymax, labels, colors):
    plt.vlines(xv, 0, y, label=label, color=color)
plt.ylabel('Fuzzy membership')
plt.xlabel('Universe variable (arb)')
plt.ylim(-0.1, 1.1)
plt.legend(loc=2)

plt.show()
