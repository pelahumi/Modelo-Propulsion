import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Lectura de la base de datos
db = pd.read_csv('DB/cars.csv', sep = ';')

#Tipos de datos
print(db.dtypes)

#Diagramas de caja y heatmap