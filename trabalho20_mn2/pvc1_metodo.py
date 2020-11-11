import numpy as np

class Elementos_Finitos:

    def __init__(self, n: int, pontos):
        self.n = n
        self.pontos = pontos

    
    def metodo(self):
        Li = 1.0/self.n # Variação dos n pontos: 1.0-0.0/n
        tam = self.n-1

        # Matriz de coeficientes
        K = np.zeros((tam,tam), dtype=float)

        # Valores para as funções de interpolação
        N_in = -1/2
        N_fim = 1/2

        k_aux1 = [[(N_in**2) * (2/Li) * 2, (N_in) * (2/Li) * (N_fim) * 2],
                  [(N_fim) * (2/Li) * (N_in) * 2, (N_fim**2) * (2/Li) * 2]]

        k_aux1 = np.matrix(k_aux1)

        k_aux2 = [[(Li/2) * (2/3), (Li/2) * (1/3)],
                  [(Li/2) * (1/3), (Li/2) * (2/3)]]

        k_aux2 = np.matrix(k_aux2)

        # Matriz de integrais usando parametrização de Legendre
        K_i = k_aux1 + k_aux2
        # K_i[0,0] = K_i[1,1] e K_i[0,1] = K_i[1,0] 

        # Montagem da matriz de coeficientes
        for i in range (0, tam):
            if i > 0:
                K[i][i-1] = K_i[0, 1]
            
            K[i][i] = 2*K_i[0, 0]
            
            if i < tam-1:
                K[i][i+1] = K_i[0, 1]

        # Vetor a direita
        B = np.zeros(tam)
        B[tam-1] = -K_i[0, 1]

        # Resolução do sistema de equações K*U = B
        sol_aprox = np.linalg.solve(K, B)
        sol_exata = self.sol_exata()

        return sol_aprox, sol_exata

    
    def sol_exata(self):
        sol_exata = [0] * (self.n-1)
        for i in range(self.n-1):
            x = self.pontos[i]
            sol_exata[i] = (np.exp(-x) - np.exp(x))/(np.exp(-1)-np.exp(1))

        return sol_exata