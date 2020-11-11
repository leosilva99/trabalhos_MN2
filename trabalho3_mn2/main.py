from math import sin
from formulas import Form_Fechadas, Form_Abertas
from particionar import Particao

def funcao(y):
    valor = ((sin(2*y) + (4*(y**2)) + 3*y)**2)
    return valor

def calcPaticoes(limiteInf, limiteSup, precisao, formula):
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
            f.append(formula(limiteInf + i*h1, limiteInf + (i+1)*h1))
            soma_atual = soma_atual + f[i]
        prec = abs(soma_atual - soma_antes)
        n = n + 1
        soma_antes = soma_atual
        f.clear()
    print('Valor da integral: {}'.format(soma_atual))
    print('Numero de iterações: {}'.format(cont))

PRECISAO = 10**(-6)
LIMITE_INF = 0
LIMITE_SUP = 0.2

formulas = Form_Fechadas(funcao)
print('Formulas fechadas')
print('Intervalo de integração: [{}, {}]'.format(LIMITE_INF, LIMITE_SUP))
print('Precisão: {}'.format(PRECISAO))
print('Trapezio')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.trapezio)
print('')

print('Simpson 1/3')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.simpson)
print('')

print('Simpson 3/8')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.simpson2)
print('')

print('Fórmula nova')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.form_nova)
print('')

formulas = Form_Abertas(funcao)
print('===================================================')
print('Formulas abertas')
print('Intervalo de integração: ({}, {})'.format(LIMITE_INF, LIMITE_SUP))
print('Precisão: {}'.format(PRECISAO))
print('Trapezio')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.trapezio)
print('')

print('Milne')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.milne)
print('')

print('Grau 3')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.sem_nome)
print('')

print('Fórmula nova aberta')
calcPaticoes(LIMITE_INF, LIMITE_SUP, PRECISAO, formulas.form_nova)
print('')

