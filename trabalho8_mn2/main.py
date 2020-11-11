from quadratura import Area_de_Superficie


def main():
    i = Area_de_Superficie()
    c = i.gauss_legendre()
    print(c)


if __name__ == "__main__":
    main()
