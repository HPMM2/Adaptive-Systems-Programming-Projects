# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:36:45 2020

@author: Sara
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


df = pd.read_csv("wine_dataset.csv")
kmeans = KMeans(n_clusters=3)
clusters=kmeans.fit_predict(df)

print("*** CENTROIDES ***")
print(kmeans.cluster_centers_)
print(kmeans.labels_)

num_objs_por_gpo = np.bincount(clusters)

for i, num_objs in enumerate(num_objs_por_gpo):
    print(f"Total de objetos en el grupo {i}: {num_objs}")


