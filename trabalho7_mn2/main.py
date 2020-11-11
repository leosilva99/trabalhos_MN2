from estrategia import Funcoes
from funcoes import func2_exp_simples, func2_exp_dupla

def main():
    c = Funcoes()
    print("Exponencial Simples para função 2")
    c.exp_simples_func2(func2_exp_simples)
    print("Exponencial Dupla para função 2")
    c.exp_dupla_func2(func2_exp_dupla)

if __name__ == "__main__":
    main()