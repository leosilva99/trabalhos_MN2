from math import sqrt, pi, sin, cos

class Area_de_Superficie:
    
    def funcao(self, a, b):                     # Função que define a superfície do problema
        result = sqrt(102400*((1+a)**2)*((((cos(pi+pi*b)**2)-(sin(pi+pi*b)**2))**2)+((sin(2*(pi+pi*b)))**2))+1)
        return result

    
    def gauss_legendre(self):                   # Quadratura de 3 pontos para o cálculo da área da superfície
        a = [-sqrt(3/5), 0, sqrt(3/5)]          # Vetor com os parâmetros para funcao(self, a, b)
        w = [5/9, 8/9, 5/9]                     # Vetor com os pesos
        fx = []      # Vetor com os diversos resultados de funcao(self, a, b)
        soma = 0
        k = 0        # Variável para ajudar a percorrer o vetor fx
        for i in range(3):
            for j in range(3):
                fx.append(self.funcao(a[j], a[i]))
                print("{}".format(fx[k]))
                soma = soma + (fx[k]*w[i]*w[j])
                k = k + 1
        print('\n')
        print(soma)
        resultado = (pi/2)*soma
        fx.clear
        print('\n')
        return resultado