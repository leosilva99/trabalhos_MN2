from potencia_regular import Potencia_Regular

def main():
    v0_a1 = [1, 0, 0]
    v0_a2 = [1, 0, 0, 0, 0]
    a1 = [[5, 2, 1], [2, 3, 1], [1, 1, 2]]
    a2 = [[40, 8, 4, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]]
    obj1 = Potencia_Regular(a1, v0_a1, 0.00001, 3)
    obj2 = Potencia_Regular(a2, v0_a2, 0.00001, 5)
    lambda1_a1, x1_a1 = obj1.metodo()
    lambda1_a2, x1_a2 = obj2.metodo()
    print("Par autovalor-autovetor da matriz A1")
    print("{}, ({}, {}, {})".format(lambda1_a1, x1_a1[0], x1_a1[1], x1_a1[2]))
    print("\r")
    print("Par autovalor-autovetor da matriz A2")
    print("{}, ({}, {}, {}, {}, {})".format(lambda1_a2, x1_a2[0], x1_a2[1], x1_a2[2],x1_a2[3], x1_a2[4]))


if __name__ == "__main__":
    main()
