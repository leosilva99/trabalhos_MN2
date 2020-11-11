class Form_Fechadas:

    def __init__(self, funcao):
        self.fx = [] # lista que receberá os valores da função que vai ser integrada
        self.h = 0 # o mesmo h da fórmula do livro
        self.funcao = funcao

    # loop para fazer os cálculos com a função e jogar na lista de valores
    def loop(self, x1, x2, num): # num recebe o número de pontos interpolados
        self.h = ((x2 - x1)/(num-1))
        for i in range(num):
            x = (x1 + (i*self.h)) # x é o valor do ponto a ser jogado na função
            self.fx.append(self.funcao(x))

    
    def trapezio(self, x1, x2):
        self.loop(x1, x2, 2)
        integ = (self.h/2) * (self.fx[0] + self.fx[1])
        self.fx.clear()
        return integ


    def simpson(self, x1, x2):
        self.loop(x1, x2, 3)
        integ = (self.h/3)*(self.fx[0] + 4*self.fx[1] + self.fx[2])
        self.fx.clear()
        return integ

    
    def simpson2(self, x1, x2):
        self.loop(x1, x2, 4)
        integ = (3*self.h/8) * (self.fx[0] + 3*self.fx[1] + 3*self.fx[2] + self.fx[3])
        self.fx.clear()
        return integ


    def form_nova(self, x1, x2):
        self.loop(x1, x2, 5)
        integ = (2*self.h/45) * (7*self.fx[0] + 32*self.fx[1] + 12*self.fx[2] + 32*self.fx[3] + 7*self.fx[4])
        self.fx.clear()
        return integ

    
class Form_Abertas:

    def __init__(self, funcao):
        self.fx = [0, 0, 0, 0, 0]
        self.h = 0
        self.funcao = funcao


    def loop(self, x1, x2, num):
        self.h = ((x2 - x1)/(num-1))
        for i in range(1, num-1):
            x = (x1 + (i*self.h))
            self.fx[i-1] = self.funcao(x)

    
    def trapezio(self, x1, x2):
        self.loop(x1, x2, 4)
        integ = (3*self.h/2) * (self.fx[0] + self.fx[1])
        return integ


    def milne(self, x1, x2):
        self.loop(x1, x2, 5)
        integ = (4*self.h/3)*(2*self.fx[0] + (-self.fx[1]) + 2*self.fx[2])
        return integ

    
    def sem_nome(self, x1, x2):
        self.loop(x1, x2, 6)
        integ = (5*self.h/24) * (11*self.fx[0] + self.fx[1] + self.fx[2] + 11*self.fx[3])
        return integ


    def form_nova(self, x1, x2):
        self.loop(x1, x2, 7)
        integ = (3*self.h/10) * ((-11*self.fx[0]) + 74*self.fx[1] - 84*self.fx[2] + 30*self.fx[3] + 11*self.fx[4])
        return integ