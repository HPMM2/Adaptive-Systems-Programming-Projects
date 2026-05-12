#!/usr/bin/env python
# coding: utf-8

# # Redes multicapa

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


datos=pd.read_csv("parkinsons.csv",header=None)
datos.head()

datos = pd.read_csv("parkinsons.csv")

datos = datos.drop("name", axis=1)


# Dividir los datos en características (X) y etiquetas (y)
X = datos.drop("status", axis=1).to_numpy()
y = datos["status"].to_numpy()


# Extrae las características del conjunto de datos
X = datos.to_numpy()[1:, 1:]

# Extrae las etiquetas (clases)
y = datos.to_numpy()[1:, 16]


# Muestra las primeras cinco filas de características
print("=== CARACTERÍSTICAS (primeras líneas) ===")
print(X[:5])

# Muestra las primeras siete etiquetas
print(y[:7])


# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


print("=== ESTANDARIZADO ===")
print(" +++ Conjunto de Entrenamiento +++")
print(X_train[:10])

print(" +++ Conjunto de Prueba +++")
print(X_test[:10])



# Crear y entrenar el modelo MLP
clf = MLPClassifier(random_state=42, max_iter=700, hidden_layer_sizes=(100, 100))
clf.fit(X_train, y_train)

# Evaluar el modelo
accuracy = round(clf.score(X_test, y_test), 3)
print("***Exactitud: ", accuracy, "***")