from potencia_regular import Potencia_Regular
from potencia_inversa import Potencia_Inversa
from potencia_com_deslocamento import Potencia_Com_Deslocamento

def main():
    v0_a1 = [1, 0, 0]
    v0_a2 = [1, 0, 0]
    v0_a3 = [1, 0, 0, 0, 0]
    a1 = [[5, 2, 1], [2, 3, 1], [1, 1, 2]]
    a2 = [[-14, 1, -2], [1, -1, 1],[-2, 1, -11]]
    a3 = [[40, 8, 4, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]]

    # Matriz A1
    obj_PR_a1 = Potencia_Regular(a1, v0_a1, 0.00001, 3)
    obj_PD_a1 = Potencia_Com_Deslocamento(a1, v0_a1, 0.00001, 3)
    obj_PI_a1 = Potencia_Inversa(a1, v0_a1, 0.00001, 3)
    lambda1_PR_a1, x1_PR_a1 = obj_PR_a1.metodo()
    lambda1_PD_a1, x1_PD_a1 = obj_PD_a1.run()
    lambda1_PI_a1, x1_PI_a1 = obj_PI_a1.metodo_inverso()

    # Matriz A2
    obj_PR_a2 = Potencia_Regular(a2, v0_a2, 0.00001, 3)
    obj_PD_a2 = Potencia_Com_Deslocamento(a2, v0_a2, 0.00001, -7)
    obj_PI_a2 = Potencia_Inversa(a2, v0_a2, 0.00001, 3)
    lambda1_PR_a2, x1_PR_a2 = obj_PR_a2.metodo()
    lambda1_PD_a2, x1_PD_a2 = obj_PD_a2.run()
    lambda1_PI_a2, x1_PI_a2 = obj_PI_a2.metodo_inverso()

    # Matriz A3
    obj_PR_a3 = Potencia_Regular(a3, v0_a3, 0.00001, 5)
    obj_PD1_a3 = Potencia_Com_Deslocamento(a3, v0_a3, 0.00001, 30)
    obj_PD2_a3 = Potencia_Com_Deslocamento(a3, v0_a3, 0.00001, 20)
    obj_PD3_a3 = Potencia_Com_Deslocamento(a3, v0_a3, 0.00001, 8)
    obj_PI_a3 = Potencia_Inversa(a3, v0_a3, 0.00001, 5)
    lambda1_PR_a3, x1_PR_a3 = obj_PR_a3.metodo()
    lambda1_PD1_a3, x1_PD1_a3 = obj_PD1_a3.run()
    lambda1_PD2_a3, x1_PD2_a3 = obj_PD2_a3.run()
    lambda1_PD3_a3, x1_PD3_a3 = obj_PD3_a3.run()
    lambda1_PI_a3, x1_PI_a3 = obj_PI_a3.metodo_inverso()

    print("Matriz A1")
    print("\r")
    print("{}, ({}, {}, {})".format(lambda1_PR_a1, x1_PR_a1[0], x1_PR_a1[1], x1_PR_a1[2]))
    print("\r")
    print("{}, ({}, {}, {})".format(lambda1_PD_a1, x1_PD_a1[0], x1_PD_a1[1], x1_PD_a1[2]))
    print("\r")
    print("{}, ({}, {}, {})".format(lambda1_PI_a1, x1_PI_a1[0], x1_PI_a1[1], x1_PI_a1[2]))

    print("\n")

    print("Matriz A2")
    print("\r")
    print("{}, ({}, {}, {})".format(lambda1_PR_a2, x1_PR_a2[0], x1_PR_a2[1], x1_PR_a2[2]))
    print("\r")
    print("{}, ({}, {}, {})".format(lambda1_PD_a2, x1_PD_a2[0], x1_PD_a2[1], x1_PD_a2[2]))
    print("\r")
    print("{}, ({}, {}, {})".format(lambda1_PI_a2, x1_PI_a2[0], x1_PI_a2[1], x1_PI_a2[2]))

    print("\n")

    print("Matriz A3")
    print("\r")
    print("{}, ({}, {}, {}, {}, {})".format(lambda1_PR_a3, x1_PR_a3[0], x1_PR_a3[1], x1_PR_a3[2], x1_PR_a3[3], x1_PR_a3[4]))
    print("\r")
    print("{}, ({}, {}, {}, {}, {})".format(lambda1_PD1_a3, x1_PD1_a3[0], x1_PD1_a3[1], x1_PD1_a3[2], x1_PD1_a3[3], x1_PD1_a3[4]))
    print("\r")
    print("{}, ({}, {}, {}, {}, {})".format(lambda1_PD2_a3, x1_PD2_a3[0], x1_PD2_a3[1], x1_PD2_a3[2], x1_PD2_a3[3], x1_PD2_a3[4]))
    print("\r")
    print("{}, ({}, {}, {}, {}, {})".format(lambda1_PD3_a3, x1_PD3_a3[0], x1_PD3_a3[1], x1_PD3_a3[2], x1_PD3_a3[3], x1_PD3_a3[4]))
    print("\r")
    print("{}, ({}, {}, {}, {}, {})".format(lambda1_PI_a3, x1_PI_a3[0], x1_PI_a3[1], x1_PI_a3[2], x1_PI_a3[3], x1_PI_a3[4]))
    print("\r")

if __name__ == "__main__":
    main()
