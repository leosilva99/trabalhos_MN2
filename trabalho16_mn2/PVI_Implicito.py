class PVI_Implicito:
    
    def __init__(self, delta_t):
        self.v0 = 5.0 # velocidade inicial(m/s)
        self.y0 = 200.0 # posição inicial(m)
        self.k = 0.25 # constante de proporcionalidade(kg/s)
        self.m = 2 # massa(kg)
        self.g = 10 # aceleração gravitacional(m/s^2)
        self.delta_t = delta_t


    def pontos_criticos1(self):
        tempo = 0.0 # a variável guarda o tempo decorrido de 0s até o momento atual da partícula
        v_ant = self.v0 # variável que guardará a velocidade a cada iteração
        y_ant = self.y0 # variável que guardará a altura a cada iteração
        y_atual = y_ant

        while(y_atual > 0): # testar se a altura já é suficientemente perto de 0m(nível do mar)
            v_atual, y_atual = self.euler_implicito(v_ant, y_ant)
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
    
    # Solução aproximada do PVI usando Euler Explícito
    def euler_implicito(self, v_antigo, y_antigo):
        v_atual = (self.m * (v_antigo - self.g * self.delta_t)) / (self.m + self.k * self.delta_t)
        y_atual = y_antigo + (self.m * self.delta_t * ( v_antigo - self.g * self.delta_t)) / ( self.m + self.k * self.delta_t )
        return v_atual, y_atual