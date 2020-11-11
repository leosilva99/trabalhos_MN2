class RungeKutta:

    def __init__(self, delta_t):
        self.v0 = 5.0 # velocidade inicial(m/s)
        self.y0 = 200.0 # posição inicial(m)
        self.k = 0.25 # constante de proporcionalidade(kg/s)
        self.m = 2 # massa(kg)
        self.g = 10 # aceleração gravitacional(m/s^2)
        self.delta_t = delta_t

    
    def pontos_criticos(self):
        tempo = 0.0 # a variável guarda o tempo decorrido de 0s até o momento atual da partícula
        v_ant = self.v0 # variável que guardará a velocidade a cada iteração
        y_ant = self.y0 # variável que guardará a altura a cada iteração
        y_atual = y_ant

        while(y_atual > 0): # testar se a altura já é suficientemente perto de 0m(nível do mar)
            v_atual, y_atual = self.sol_aproximada(v_ant, y_ant)
            tempo = tempo + self.delta_t

            if(v_atual*v_ant < 0): # altura máxima: v(t) = 0 m/s
                if(y_ant > y_atual):
                    y_alt_max = y_ant # altura máxima da trajetória
                    t_alt_max = tempo - self.delta_t # momento em que alcançou a altura máxima
                else:
                    y_alt_max = y_atual # altura máxima da trajetória
                    t_alt_max = tempo # momento em que alcançou a altura máxima
            
            if(y_atual*y_ant < 0): # fim da trajetória: y(t) = 0 m
                v_mar = v_ant # velocidade quando chegou ao mar
                t_mar = tempo - self.delta_t # tempo total da trajetória

            v_ant = v_atual
            y_ant = y_atual
        
        return y_alt_max, t_alt_max, v_mar, t_mar

    
    def auxiliar1(self, v_ant):
        result1 = [0] * 2 # posição 0: velocidade, posição 1: altura

        # Equação 47
        result1[0] = -self.g - ((self.k/self.m)*v_ant)
        result1[1] = v_ant

        return result1

    
    def auxiliar2(self, v_ant):
        auxiliar1 = self.auxiliar1(v_ant)

        # Equação 48
        v_aux2 = v_ant + (self.delta_t/2)*auxiliar1[0]
        
        # Equação 49
        result2 = self.auxiliar1(v_aux2) # posição 0: velocidade, posição 1: altura

        return result2

    
    def auxiliar3(self, v_ant):
        auxiliar1 = self.auxiliar1(v_ant)
        auxiliar2 = self.auxiliar2(v_ant)

        # Equação 50
        v_aux3 = v_ant + self.delta_t*(-auxiliar1[0] + 2*auxiliar2[0])

        # Equação 51
        result3 = self.auxiliar1(v_aux3) # posição 0: velocidade, posição 1: altura

        return result3

    
    def sol_aproximada(self, v_ant, y_ant):
        auxiliar1 = self.auxiliar1(v_ant)
        auxiliar2 = self.auxiliar2(v_ant)
        auxiliar3 = self.auxiliar3(v_ant)

        result = [0] * 2 # posição 0: velocidade, posição 1: altura

        # Equação 52
        result[0] = v_ant + self.delta_t*((auxiliar1[0] + 4*auxiliar2[0] + auxiliar3[0])/6)
        result[1] = y_ant + self.delta_t*((auxiliar1[1] + 4*auxiliar2[1] + auxiliar3[1])/6)

        return result[0], result[1] 