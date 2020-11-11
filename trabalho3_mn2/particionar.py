from math import sin
from formulas import Form_Fechadas


class Particao:
    def trapezio(x1, x2):
        f = []
        obj = Form_Fechadas()
        soma_antes = 0
        soma_atual = 0
        cont = 0
        n = 1
        prec = 1
        while prec > (10**(-6)):
            h1 = (x2-x1)/n
            for i in range(n):
                f.append(obj.trapezio(x1 + i*h1, x1 + (i+1)*h1))
                soma_atual = soma_atual + f[i]
            prec = abs(soma_atual - soma_antes)
            if prec <= (10**(-6)):
                return cont
            cont = cont + 1
            n = n + 1
            soma_antes = soma_atual
            soma_atual = 0
            f.clear()
