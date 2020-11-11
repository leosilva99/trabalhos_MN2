from math import sin

def funcao(x):
    result = ((sin(2*x) + (4*(x**2)) + (3*x))**2)
    return result

def func_aux(xi, xf, x):
    result = (((xi+xf)/2) + (((xf-xi)/2)*x))
    return result