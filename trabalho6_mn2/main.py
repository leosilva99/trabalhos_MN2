from hermite import Hermite
from laguerre import Laguerre
from chebyshev import Chebyshev

def main():
    x1 = Hermite()
    print('Hermite grau 2')
    print(x1.grau2())
    print('Hermite grau 3')
    print(x1.grau3())
    print('Hermite grau 4')
    print(x1.grau4())
    print("\n")

    laguerre = Laguerre()
    print('Laguerre grau 2')
    print(laguerre.grau2())
    print('Laguerre grau 3')
    print(laguerre.grau3())
    print('Laguerre grau 4')
    print(laguerre.grau4())
    print("\n")

    chebyshev = Chebyshev()
    print('Chebyshev grau 2')
    print(chebyshev.grau2())
    print('Chebyshev grau 3')
    print(chebyshev.grau3())
    print('Chebyshev grau 4')
    print(chebyshev.grau4())

if __name__ == "__main__":
    main()
