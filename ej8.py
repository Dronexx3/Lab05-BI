import numpy as np
from scipy import stats
# Datos de ejemplo 
data = [10, 12, 23, 23, 16, 23, 21, 16]
# Calcular la variación
variation = stats.variation(data)
print(f"Variación: {variation}")