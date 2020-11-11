from funcao import funcao
from math import sqrt, cos, pi

class Chebyshev:
    
    def loop(self, x, w, num):
        fx = []
        soma = 0
        for i in range(num):
            fx.append(funcao(x[i]))
            soma = soma + (fx[i]*w[i])
        fx.clear
        return soma


    def grau2(self):
        x = [-1/sqrt(2), 1/sqrt(2)]   # raizes do polinomio chebyshev
        w = [pi/2, pi/2]              # pesos
        result = self.loop(x, w, 2)
        return result


    def grau3(self):
        x = [-sqrt(3)/2, 0, sqrt(3)/2]
        w = [pi/3, pi/3, pi/3]
        result = self.loop(x, w, 3)
        return result

    
    def grau4(self):
        x = [-0.92387953251, -0.38268343236, 0.38268343236,0.92387953251, ]
        w = [pi/4, pi/4, pi/4, pi/4]
        result = self.loop(x, w, 4)
        return result