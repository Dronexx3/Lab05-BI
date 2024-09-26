from river import anomaly

# Definir una clase personalizada para el detector de anomalías
class AnomalyDetector:
    def __init__(self):  # Corregido _init_ a __init__
        self.model = anomaly.OneClassSVM()

    def entrenar(self, datos):
        self.model.learn_one(datos)

    def detectar(self, datos):
        return self.model.score_one(datos)

# Crear una instancia del detector de anomalías
detector = AnomalyDetector()

# Datos de entrenamiento y entrenamiento del modelo
datos_para_entrenar = {'caracteristica_a': 1, 'caracteristica_b': 2}
detector.entrenar(datos_para_entrenar)

# Lista de diferentes conjuntos de datos para detectar anomalías
datos_para_detectar = [
    {'caracteristica_a': 3, 'caracteristica_b': 4},
    {'caracteristica_a': 5, 'caracteristica_b': 6},
    {'caracteristica_a': 10, 'caracteristica_b': 20},
]

# Detectar anomalías en cada conjunto de datos
for i, datos in enumerate(datos_para_detectar, 1):
    resultado_anomalia = detector.detectar(datos)
    print(f"Resultado de detección de anomalía para conjunto {i}: {resultado_anomalia}")
