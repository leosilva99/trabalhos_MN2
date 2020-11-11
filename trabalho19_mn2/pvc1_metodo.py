import numpy as np

class Diferencas_Finitas_PVC1:
    def __init__(self, n: int, pontos):
        self.n = n
        self.pontos = pontos # n - 1 pontos discretos no intervalo [0, 1]


    def metodo(self):
        delta_x = 1.0/self.n # Variação do domínio: (1-0)/n
        tam = self.n-1 # Número de pontos

        # Máscara dos coeficientes
        centro = -(2/(delta_x**2) + 1)
        borda = 1/(delta_x**2)

        # Posicionar os coeficientes na matriz
        matrix_A = np.zeros((tam, tam))

        for i in range(tam):
            if i > 0:
                matrix_A[i][i-1] = borda
            
            matrix_A[i][i] = centro
            
            if i < tam-1:
                matrix_A[i][i+1] = borda

        # Matriz resultante do sistema de equações
        matrix_b = [0] * tam
        matrix_b[tam-1] = -borda

        # matrix_A*x = matrix_b
        sol_aprox = np.linalg.solve(matrix_A, matrix_b) # Resolve o sistema de equações algébricas
        sol_exata = self.sol_exata() # Solução exata em cada ponto do intervalo

        return sol_aprox, sol_exata

    
    def sol_exata(self):
        sol_exata = [0] * (self.n-1)
        for i in range(self.n-1):
            x = self.pontos[i]
            sol_exata[i] = (np.exp(-x) - np.exp(x))/(np.exp(-1)-np.exp(1))

        return sol_exata

