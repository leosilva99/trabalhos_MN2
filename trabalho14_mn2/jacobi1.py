from math import sin, cos, atan, fabs, degrees, pi
import numpy as np

class Jacobi1:
    def __init__(self, matriz, n, erro):
        self.a = matriz
        self.tam = n
        self.erro = erro


    def metodo(self):
        P = np.identity(self.tam, dtype=float)
        J = np.identity(self.tam, dtype=float)
        np.set_printoptions(suppress=True)
        A_velha = self.a
        A_nova = self.a
        lamb = [0] * self.tam
        val = 100

        while(val > self.erro):
            A_nova, J = self.varreduraJacobi(A_velha)
            A_velha = A_nova
            P = P.dot(J)
            val = self.soma_quadrados(A_nova)

        for i in range(self.tam):
            lamb[i] = A_nova[i][i]

        return P, lamb, A_nova

    
    def varreduraJacobi(self, A):
        J = np.identity(self.tam, dtype=float)
        A_velha = A
        A_nova = A
        
        
        for j in range(0, self.tam-1):
            for i in range(j+1, self.tam):
                J_ij = self.matrizJacobi(A_velha, i, j)
                aux1 = np.transpose(J_ij).dot(A_velha)
                A_nova = aux1.dot(J_ij)
                A_velha = A_nova
                aux2 = J
                J = aux2.dot(J_ij)
                print("Matriz A_nova da iteração ({},{})\n".format(i, j))
                print(A_nova)
                print("\n")
                print("Matriz J da iteração ({},{})\n".format(i, j))
                print(J)
                print("\n")

        
        return A_nova, J


    def matrizJacobi(self, A, i, j):
        J_ij = np.identity(self.tam, dtype=float)
        ang = 0
        erro = 10**(-6)

        if(fabs(A[i][j]) <= erro):
            return J_ij
        
        if(fabs(A[i][i] - A[j][j]) <= erro):
            ang = pi/4
        else:
            ang = (1/2)*atan((-2*A[i][j])/(A[i][i]-A[j][j]))
        
        J_ij[i][i] = cos(ang)
        J_ij[j][j] = cos(ang)
        J_ij[i][j] = sin(ang)        
        J_ij[j][i] = -sin(ang)

        return J_ij


    def soma_quadrados(self, A):
        soma = 0
        for j in range(0, self.tam-1):
            for i in range(j+1, self.tam):
                soma = soma + (A[i][j]*A[i][j])
        
        return soma
