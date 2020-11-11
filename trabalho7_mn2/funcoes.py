from math import sinh, cosh, tanh, pi, sqrt

def func2_exp_simples(x):
    result = 1/(pow(cosh(x), 2)*sqrt(4 - pow(-1 + tanh(x), 2)))
    return result

def func2_exp_dupla(x):
    result = (cosh(x)*pi)/(2*pow(cosh((pi*sinh(x))/2), 2)*sqrt(4 - pow(-1 + tanh((pi*sinh(x))/2), 2)))
    return result

def func_aux(xi, xf, x):
    result = (((xi+xf)/2) + (((xf-xi)/2)*x))
    return result

