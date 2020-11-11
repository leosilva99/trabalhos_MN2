def funcao(x):
    return 16*(x**4)

# qual integral se vai calcular de fato?

# hermite:  (e**(-(x*x))) * funcao           de menos infinito a mais infinito
# laguerre: (e**(-x)) * funcao               de 0 a mais infinito
# chebyshev: (1/sqrt(1-(x*x))) * funcao      de -1 a +1