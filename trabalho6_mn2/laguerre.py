from funcao import funcao
from math import sqrt

class Laguerre:
    
    def loop(self, x, w, num):
        fx = []
        soma = 0
        for i in range(num):
            fx.append(funcao(x[i]))
            soma = soma + (fx[i]*w[i])
        fx.clear
        return soma


    def grau2(self):
        x = [2 - sqrt(2), 2 + sqrt(2)]                    # raizes do polinomio de laguerre
        w = [(1/4)*(2 + sqrt(2)), (1/4)*(2 - sqrt(2))]    # pesos
        result = self.loop(x, w, 2)
        return result


    def grau3(self):
        x = [0.4157745568, 2.2942803603, 6.2899450829]
        w = [0.7110930099, 0.2785177336, 0.0103892565]
        result = self.loop(x, w, 3)
        return result

    
    def grau4(self):
        x = [0.323, 1.746, 4.537, 9.395]                                             
        w = [0.59562, 0.35697, 0.03885, 0.00053]
        result = self.loop(x, w, 4)
        return result