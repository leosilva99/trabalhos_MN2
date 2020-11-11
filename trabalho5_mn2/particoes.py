from quadraturas import Quadraturas

def calcPaticoes4(limiteInf, limiteSup, precisao):
    f = []
    soma_antes = 0
    soma_atual = 0
    cont = 0
    n = 1
    prec = 1
    while prec > (precisao):
        cont = cont + 1
        soma_atual = 0
        h1 = (limiteSup-limiteInf)/n
        for i in range(n):
            c = Quadraturas(limiteInf + i*h1, limiteInf + (i+1)*h1)
            f.append(c.grau4())
            soma_atual = soma_atual + f[i]
        prec = abs(soma_atual - soma_antes)
        n = n + 1
        soma_antes = soma_atual
        f.clear()
    print('Valor da integral: {}'.format(soma_atual))
    print('Numero de iterações: {}'.format(cont))

def calcPaticoes3(limiteInf, limiteSup, precisao):
    f = []
    soma_antes = 0
    soma_atual = 0
    cont = 0
    n = 1
    prec = 1
    while prec > (precisao):
        cont = cont + 1
        soma_atual = 0
        h1 = (limiteSup-limiteInf)/n
        for i in range(n):
            c = Quadraturas(limiteInf + i*h1, limiteInf + (i+1)*h1)
            f.append(c.grau3())
            soma_atual = soma_atual + f[i]
        prec = abs(soma_atual - soma_antes)
        n = n + 1
        soma_antes = soma_atual
        f.clear()
    print('Valor da integral: {}'.format(soma_atual))
    print('Numero de iterações: {}'.format(cont))

def calcPaticoes2(limiteInf, limiteSup, precisao):
    f = []
    soma_antes = 0
    soma_atual = 0
    cont = 0
    n = 1
    prec = 1
    while prec > (precisao):
        cont = cont + 1
        soma_atual = 0
        h1 = (limiteSup-limiteInf)/n
        for i in range(n):
            c = Quadraturas(limiteInf + i*h1, limiteInf + (i+1)*h1)
            f.append(c.grau2())
            soma_atual = soma_atual + f[i]
        prec = abs(soma_atual - soma_antes)
        n = n + 1
        soma_antes = soma_atual
        f.clear()
    print('Valor da integral: {}'.format(soma_atual))
    print('Numero de iterações: {}'.format(cont))