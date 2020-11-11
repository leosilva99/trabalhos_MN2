from particoes import *

PRECISAO = 10**(-6)
LIMITE_INF = 0
LIMITE_SUP = 1

def main():
  print('Grau 2')
  calcPaticoes2(LIMITE_INF, LIMITE_SUP, PRECISAO)
  print()
  print('Grau 3')
  calcPaticoes3(LIMITE_INF, LIMITE_SUP, PRECISAO)
  print()
  print('Grau 4')
  calcPaticoes4(LIMITE_INF, LIMITE_SUP, PRECISAO)


if __name__ == "__main__":
    main()
    

