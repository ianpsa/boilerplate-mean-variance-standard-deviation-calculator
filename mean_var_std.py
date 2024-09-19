import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3, 3)

    media_1 = np.mean(matrix, axis=0).tolist()
    media_2 = np.mean(matrix, axis=1).tolist()
    media = np.mean(matrix).tolist()

    variancia_1 = np.var(matrix, axis=0).tolist()
    variancia_2 = np.var(matrix, axis=1).tolist()
    variancia = np.var(matrix).tolist()

    desvio_1 = np.std(matrix, axis=0).tolist()
    desvio_2 = np.std(matrix, axis=1).tolist()
    desvio = np.std(matrix).tolist()

    maximo_1 = np.max(matrix, axis=0).tolist()
    maximo_2 = np.max(matrix, axis=1).tolist()
    maximo = np.max(matrix).tolist()

    minimo_1 = np.min(matrix, axis=0).tolist()
    minimo_2 = np.min(matrix, axis=1).tolist()
    minimo = np.min(matrix).tolist()

    soma_1 = np.sum(matrix, axis=0).tolist()
    soma_2 = np.sum(matrix, axis=1).tolist()
    soma = np.sum(matrix).tolist()

    calculations = {
        'mean': [media_1, media_2, media],
        'variance': [variancia_1, variancia_2, variancia],
        'standard deviation': [desvio_1, desvio_2, desvio],
        'min': [minimo_1, minimo_2, minimo],
        'max': [maximo_1, maximo_2, maximo],
        'sum': [soma_1, soma_2, soma]
    }

    return calculations