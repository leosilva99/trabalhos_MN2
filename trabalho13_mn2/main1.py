from houseHolder import MetodoHouseholder
from potencia_regular import Potencia_Regular
from potencia_com_deslocamento import Potencia_Com_Deslocamento
from potencia_inversa import Potencia_Inversa


v0 = [1, 0, 0, 0, 0]
A1 = [[40, 8, 4, 2, 1],
      [8, 30, 12, 6, 2],
      [4, 12, 20, 1, 2],
      [2, 6, 1, 25, 4],
      [1, 2, 2, 4, 5]]

houseH = MetodoHouseholder(A1, 5)

A_barra, H = houseH.metodo()

obj_PR = Potencia_Regular(A_barra, v0, 0.00001, 5)

obj_PD1 = Potencia_Com_Deslocamento(A_barra, v0, 0.00001, 30)
obj_PD2 = Potencia_Com_Deslocamento(A_barra, v0, 0.00001, 20)
obj_PD3 = Potencia_Com_Deslocamento(A_barra, v0, 0.00001, 8)

obj_PI = Potencia_Inversa(A_barra, v0, 0.00001, 5)

lambda1_PR, x1_PR = obj_PR.metodo()

lambda1_PD1, x1_PD1 = obj_PD1.run()
lambda1_PD2, x1_PD2 = obj_PD2.run()
lambda1_PD3, x1_PD3 = obj_PD3.run()

lambda1_PI, x1_PI = obj_PI.metodo_inverso()

print("Matriz A_barra do método de HouseHolder\n")
print(A_barra)
print("\n")
print("Matriz H do método de HouseHolder\n")
print(H)
print("\n")

print("Pares autovalores-autovetores da matriz A_barra\n")
print("{}, {}".format(lambda1_PR, x1_PR))
print("\r")
print("{}, {}".format(lambda1_PD1, x1_PD1))
print("\r")
print("{}, {}".format(lambda1_PD2, x1_PD2))
print("\r")
print("{}, {}".format(lambda1_PD3, x1_PD3))
print("\r")
print("{}, {}".format(lambda1_PI, x1_PI))
print("\r")

print("\n----------------------------------------------------------------------------------------\n\n")

obj_PR_A1 = Potencia_Regular(A1, v0, 0.00001, 5)

obj_PD1_A1 = Potencia_Com_Deslocamento(A1, v0, 0.00001, 30)
obj_PD2_A1 = Potencia_Com_Deslocamento(A1, v0, 0.00001, 20)
obj_PD3_A1 = Potencia_Com_Deslocamento(A1, v0, 0.00001, 8)

obj_PI_A1 = Potencia_Inversa(A1, v0, 0.00001, 5)

lambda1_PR_A1, x1_PR_A1 = obj_PR_A1.metodo()

lambda1_PD1_A1, x1_PD1_A1 = obj_PD1_A1.run()
lambda1_PD2_A1, x1_PD2_A1 = obj_PD2_A1.run()
lambda1_PD3_A1, x1_PD3_A1 = obj_PD3_A1.run()

lambda1_PI_A1, x1_PI_A1 = obj_PI_A1.metodo_inverso()

print("Pares autovalores-autovetores da matriz A\n")
print("{}, {}".format(lambda1_PR_A1, x1_PR_A1))
print("\r")
print("{}, {}".format(lambda1_PD1_A1, x1_PD1_A1))
print("\r")
print("{}, {}".format(lambda1_PD2_A1, x1_PD2_A1))
print("\r")
print("{}, {}".format(lambda1_PD3_A1, x1_PD3_A1))
print("\r")
print("{}, {}".format(lambda1_PI_A1, x1_PI_A1))
print("\r")

