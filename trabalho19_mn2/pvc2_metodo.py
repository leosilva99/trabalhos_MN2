import numpy as np

class Diferencas_Finitas_PVC2:

    def __init__(self, n: int, fxy):
        self.n = n
        self.fxy = fxy
        

    def metodo(self):
        delta_x = 1.0/self.n # Variação do domínio no eixo x: (1-0)/n
        delta_y = 1.0/self.n # Variação do domínio no eixo y: (1-0)/n
        tam = (self.n-1)**2 # Dimensão da matriz de coeficientes: tamxtam

        # Máscara dos coeficientes
        borda_x = 1/(delta_x**2)
        centro = -2 * (1/(delta_x**2) + 1/(delta_y**2))
        borda_y = 1/(delta_y**2)

        # Preencher a matriz de coeficientes
        matrix_A = np.zeros((tam, tam), dtype=float)
        k = 0
        y = 0
        for i in range(tam):
            if i > 0:
                k = k + 1
                if k%(self.n-1) != 0: 
                    matrix_A[i][i-1] = borda_y
                else:
                    matrix_A[i][i-1] = 0

            if i > (self.n-2):
                matrix_A[i][i-(self.n-1)] = borda_x

            matrix_A[i][i] = centro

            if i < tam-(self.n-1):
                matrix_A[i][i+(self.n-1)] = borda_x

            if i < tam-1:
                y = y + 1
                if y%(self.n-1) !=0: 
                    matrix_A[i][i+1] = borda_y
                else:
                    matrix_A[i][i+1] = 0

        # Preencher o vetor da direita
        matrix_B = np.empty((tam), dtype=float)
        matrix_B.fill(self.fxy)
        
        # Resolver o sistema de equações A*x = B
        matrix_A_inv = np.linalg.inv(matrix_A)
        result = np.dot(matrix_A_inv, matrix_B)
        return result