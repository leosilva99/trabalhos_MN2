from funcoes import func_aux
from math import sqrt, pi

class Funcoes:

    def loop(self, a, b, xa, w, num, funcao):
        x = []
        fx = []
        soma = 0
        for i in range(num):
            x.append(func_aux(a, b, xa[i]))
            fx.append(funcao(x[i]))
            soma = soma + (fx[i]*w[i])
        resultado = (((b - a)/2)*(soma))
        x.clear
        fx.clear
        return resultado

    
    def quadratura(self, a, b, funcao):
        xa = [-sqrt(3)/3, sqrt(3)/3]
        w = [1, 1]
        result = self.loop(a, b, xa, w, 2, funcao)
        return result


    def particoes(self, funcao, a, b):
        precisao = 10**(-6)
        f = []
        soma_anterior = 0
        soma_atual = 0
        n = 0
        prec = 1
        while prec > precisao:
            n = n + 1
            soma_atual = 0
            h1 = (b - a)/n
            for i in range(n):
                f.append(self.quadratura(a + i*h1, a + (i+1)*h1, funcao))
                soma_atual = soma_atual + f[i]
            prec = abs(soma_atual - soma_anterior)
            soma_anterior = soma_atual
            f.clear()
        print(n)
        print(soma_atual)


    def exp_simples_func2(self, funcao):
        c = 1
        while c <= 18.5:
            print("[{}, {}]".format(-c, c))
            self.particoes(funcao, -c, c)
            print('\n')
            c = c + 0.5

    
    def exp_dupla_func2(self, funcao):
        c = 1
        while c <= 3:
            print("[{}, {}]".format(-c, c))
            self.particoes(funcao, -c, c)
            print('\n')
            c = c + 0.5