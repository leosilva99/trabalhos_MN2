from jacobi2 import Jacobi2
from houseHolder import MetodoHouseholder
import numpy as np

def main():
    A = [[40, 8, 4, 2, 1],
         [8, 30, 12, 6, 2],
         [4, 12, 20, 1, 2],
         [2, 6, 1, 25, 4],
         [1, 2, 2, 4, 5]]
    
    houseHold = MetodoHouseholder(A, 5)
    MatrizT, MatrizH = houseHold.metodo()
    
    jacobi = Jacobi2(MatrizT, 5, 0.0001)
    P, lamb, A_nova = jacobi.metodo()

    print("Matriz P antes de P = H*P\n")
    print(P)
    print("\n")

    P = MatrizH.dot(P)
    
    print("Matriz P depois de P = H*P\n")
    print(P)
    print("\n")
        
    P = np.transpose(P)
    print("Pares autovalor-autovetor\n")
    for i in range(jacobi.tam):
        print("{} -> {}".format(lamb[i], P[i]))
        

if(__name__ == "__main__"):
    main()