from funcao import funcao
from math import sqrt, pi

class Hermite:
    
    def loop(self, x, w, num):
        fx = []
        soma = 0
        for i in range(num):
            fx.append(funcao(x[i]))
            soma = soma + (fx[i]*w[i])
        fx.clear
        return soma


    def grau2(self):
        x = [-1/sqrt(2), 1/sqrt(2)]    # raizes do polinomio de hermite
        w = [sqrt(pi)/2, sqrt(pi)/2]   # pesos
        result = self.loop(x, w, 2)
        return result


    def grau3(self):
        x = [-sqrt(3/2), 0, sqrt(3/2)]  
        w = [sqrt(pi)/6, 2*sqrt(pi)/3, sqrt(pi)/6]
        result = self.loop(x, w, 3)
        return result

    
    def grau4(self):
        x = [-1.651, -0.525, 0.525, 1.1651]
        w = [0.0813128354472452, 0.8049140900055128, 0.8049140900055128, 0.0813128354472452]
        result = self.loop(x, w, 4)
        return result