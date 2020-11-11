from math import sqrt

class Potencia_Regular:

    def __init__(self, a1, v0, erro, tam):   # step 1
        self.a1 = a1
        self.v0 = v0
        self.erro = erro
        self.tam = tam

   
    def metodo(self):
        vk_novo = []
        vk_velho = []
        erro = 10
        lambda1_novo = 0   # step 2
        for i in range(self.tam):   # step 3
            vk_novo.append(self.v0[i])
            vk_velho.append(0)
        
        while(erro > self.erro):
            lambda1_velho = lambda1_novo   # step 4
            vk_velho = vk_novo   # step 5
            x1_velho = self.normalizacao(vk_velho)   # step 6
            vk_novo = self.matriz_x_vetor(self.a1, x1_velho)   # step 7
            lambda1_novo = self.vetor_x_vetor(x1_velho, vk_novo)   # step 8
            erro = abs((lambda1_novo-lambda1_velho)/lambda1_novo)   # step 9

        return lambda1_novo, x1_velho


    def normalizacao(self, v):
        aux = []
        s = sqrt(self.vetor_x_vetor(v, v))
        for i in range(self.tam):
            aux.append(v[i]/s)
        return aux


    def matriz_x_vetor(self, m, v):
        x = []
        for i in range(self.tam):
            s = self.vetor_x_vetor(m[i], v)
            x.append(s)
        return x

    
    def vetor_x_vetor(self, v1, v2):
        s = 0
        for i in range(self.tam):
            s = s + v1[i]*v2[i]
        return s