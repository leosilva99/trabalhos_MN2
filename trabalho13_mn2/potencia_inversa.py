from potencia_regular import Potencia_Regular
import numpy as np

class Potencia_Inversa(Potencia_Regular):

    def metodo_inverso(self):
        a1_inv = np.linalg.inv(self.a1)   # matriz inversa de a1
        aux = Potencia_Regular(a1_inv, self.v0, self.erro, self.tam)
        lambda1_novo, x1_velho = aux.metodo()   # step 1 ao step 10
        lambda_n = 1/lambda1_novo   # step 11
        return lambda_n, x1_velho