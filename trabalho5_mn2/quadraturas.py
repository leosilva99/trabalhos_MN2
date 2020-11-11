from math import sqrt
from funcao import funcao, func_aux

class Quadraturas:

    def __init__(self, xi, xf):
        self.xi = xi
        self.xf = xf

    
    def loop(self, a, w, num):
        x = []
        fx = []
        soma = 0
        for i in range(num):
            x.append(func_aux(self.xi, self.xf, a[i]))
            fx.append(funcao(x[i]))
            soma = soma + (fx[i]*w[i])
        resultado = (((self.xf - self.xi)/2)*(soma))
        x.clear
        fx.clear
        return resultado


    def grau2(self):
        a = [-sqrt(3)/3, sqrt(3)/3]
        w = [1, 1]
        result = self.loop(a, w, 2)
        return result


    def grau3(self):
        a = [-sqrt(3/5), 0, sqrt(3/5)]
        w = [5/9, 8/9, 5/9]
        result = self.loop(a, w, 3)
        return result

    
    def grau4(self):
        a = [-sqrt((15+(2*sqrt(30)))/35), -sqrt((15-(2*sqrt(30)))/35), sqrt((15-(2*sqrt(30)))/35), sqrt((15+(2*sqrt(30)))/35)]
        w = [((18-sqrt(30))/36), ((18+sqrt(30))/36), ((18+sqrt(30))/36), ((18-sqrt(30))/36)]
        result = self.loop(a, w, 4)
        return result