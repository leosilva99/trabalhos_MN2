from pvc2_metodo import Diferencas_Finitas_PVC2

def main():
    pontos = [0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875]
    sol = Diferencas_Finitas_PVC2(8, 4)
    
    sol_aprox = sol.metodo()
    
    print("Método de Diferenças Finitas - PVC1\n")
    print("----------------------------------")
    print("|      |   Solução aproximada    |")
    print("----------------------------------")
    for i in range(49):
        print("|  y{}  |   {:.8f}           |".format(i+1, sol_aprox[i]))
        print("----------------------------------")


if __name__ == "__main__":
    main()    