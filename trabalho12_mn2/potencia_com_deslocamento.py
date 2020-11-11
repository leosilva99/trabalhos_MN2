from potencia_inversa import Potencia_Inversa
import numpy as np

class Potencia_Com_Deslocamento:
    def __init__(self, matriz, v0, erro, deslocamento):   # step 1
        self.matriz = matriz
        self.v0 = v0
        self.erro = erro
        self.deslocamento = deslocamento

        self.dimensaoMatriz = len(matriz)
        self.matrizIdentidade = np.identity(self.dimensaoMatriz, dtype=int) # TODO mudar dinamicamente

    def run(self):
        matrizNova = np.subtract(self.matriz, np.multiply(self.deslocamento, self.matrizIdentidade))
        potenciaInversa = Potencia_Inversa(matrizNova, self.v0, self.erro, self.dimensaoMatriz)
        lambd, x = potenciaInversa.metodo_inverso()
        return lambd + self.deslocamento, x

        
