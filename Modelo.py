import numpy as np

class Modelo:
    def __init__(self, nome, precisao, recall, acuracia, matriz_confusao):
        self.nome = nome
        self.precisao = precisao
        self.recall = recall
        self.acuracia = acuracia
        self.matriz_confusao = matriz_confusao

    def matrizConfusao(y_true, y_pred):
        classes = [1,2,3,4]
        matrix = np.zeros((len(classes), len(classes)), dtype=int)
        for true, pred in zip(y_true, y_pred):
            matrix[true-1, pred-1] += 1
    
        return matrix
    
    def preditivo(y_true, y_pred):
        matriz = Modelo.matrizConfusao(y_true, y_pred)
        classes = matriz.shape[0]

        acuracia = np.trace(matriz) / np.sum(matriz)

        precisao_classes = []
        recall_classes = []

        for i in range(classes):
            TP = matriz[i,i]
            FP = np.sum(matriz[:,i]) - TP
            FN = np.sum(matriz[i,:]) - TP

        precisao = TP/(TP+FP) if (TP+FP)!=0 else 0
        precisao_classes.append(precisao)

        recall = TP/(TP+FN) if (TP+FN)!=0 else 0
        recall_classes.append(precisao)

        return acuracia, recall_classes, precisao_classes
