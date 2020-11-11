from PreditorCorretor import PreditorCorretor

def main():
    print("Solução aproximada do PVI utilizando o método de Preditor-Corretor de 4º ordem\n")
    print("--------------------------------------------------------------------------------------------------")
    print("|   delta_t(s)   |   alt_max(m)   |   temp_alt_max(s)   |   vel_final(m/s)   |   temp_final(s)   |")
    print("--------------------------------------------------------------------------------------------------")

    for i in range(1, 5):
        sol = PreditorCorretor(10**(-i))
        y_alt_max, t_alt_max, v_mar, t_mar = sol.pontos_criticos()
        print("    {}              {:.4f}         {:.4f}                {:.4f}             {:.4f}"
        .format(10**(-i), y_alt_max, t_alt_max, v_mar, t_mar))
        print("--------------------------------------------------------------------------------------------------")


if(__name__ == "__main__"):
    main()