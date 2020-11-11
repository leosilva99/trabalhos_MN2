class PreditorCorretor:

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

        estados_ant = self.inicializacao()

        while(y_atual > 0): # testar se a altura já é suficientemente perto de 0m(nível do mar)
            v_atual, y_atual = self.PredicaoCorrecao(estados_ant)
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

            aux  = estados_ant[2:]
            aux.append(v_atual)
            aux.append(y_atual)
            estados_ant = aux

            v_ant = v_atual
            y_ant = y_atual
        
        return y_alt_max, t_alt_max, v_mar, t_mar


    def PredicaoCorrecao(self, estados_ant):
        auxiliar1 = self.auxiliar1(estados_ant[0]) # Fi-3
        auxiliar2 = self.auxiliar1(estados_ant[2]) # Fi-2
        auxiliar3 = self.auxiliar1(estados_ant[4]) # Fi-1
        auxiliar4 = self.auxiliar1(estados_ant[6]) # Fi

        predicao = [0] * 2

        # Fórmula de predição de quarta ordem
        predicao[0] = estados_ant[6] + (self.delta_t/24)*(-9*auxiliar1[0] + 33*auxiliar2[0] - 59*auxiliar3[0] + 55*auxiliar4[0])
        predicao[1] = estados_ant[7] + (self.delta_t/24)*(-9*auxiliar1[1] + 33*auxiliar2[1] - 59*auxiliar3[1] + 55*auxiliar4[1])

        correcao = [0] * 2
        auxiliar_pred = self.auxiliar1(predicao[0]) # F_predicao

        # Fórmula de correção de quarta ordem
        correcao[0] = estados_ant[6] + (self.delta_t/24)*(auxiliar2[0] - 5*auxiliar3[0] + 19*auxiliar4[0] + 9*auxiliar_pred[0])
        correcao[1] = estados_ant[7] + (self.delta_t/24)*(auxiliar2[1] - 5*auxiliar3[1] + 19*auxiliar4[1] + 9*auxiliar_pred[1])

        return correcao[0], correcao[1]

    
    # Obtém estados S1, S2 e S3 pelo método de Runge-Kutta de terceira ordem.
    def inicializacao(self):
        v_ant = self.v0
        y_ant = self.y0

        estados = self.sol_aproximada(v_ant, y_ant)

        return estados


    def auxiliar1(self, v_ant):
        result1 = [0] * 2 # posição 0: velocidade, posição 1: altura

        # Equação T1
        result1[0] = -self.g - ((self.k/self.m)*v_ant)
        result1[1] = v_ant

        return result1

    
    def auxiliar2(self, v_ant):
        auxiliar1 = self.auxiliar1(v_ant)

        # Equação T2
        v_aux2 = v_ant + (self.delta_t/2)*auxiliar1[0]
        
        # Equação T3
        result2 = self.auxiliar1(v_aux2) # posição 0: velocidade, posição 1: altura

        return result2

    
    def auxiliar3(self, v_ant):
        auxiliar2 = self.auxiliar2(v_ant)

        # Equação T4
        v_aux3 = v_ant + (self.delta_t/2)*auxiliar2[0]

        # Equação T5
        result3 = self.auxiliar1(v_aux3) # posição 0: velocidade, posição 1: altura

        return result3


    def auxiliar4(self, v_ant):
        auxiliar3 = self.auxiliar3(v_ant)

        # Equação T6
        v_aux4 = v_ant + self.delta_t*auxiliar3[0]

        # Equação T7
        result4 = self.auxiliar1(v_aux4)

        return result4


    def sol_aproximada(self, v_ant, y_ant):
        estados = [0] * 8
        # posições 0 e 1: S0 (posição 0: velocidade, posição 1: altura)
        # posições 2 e 3: S1 (posição 2: velocidade, posição 3: altura)
        # posições 4 e 5: S2 (posição 4: velocidade, posição 5: altura)
        # posições 6 e 7: S3 (posição 4: velocidade, posição 5: altura)

        estados[0] = v_ant
        estados[1] = y_ant

        i=1
        while(i < 4):
            auxiliar1 = self.auxiliar1(v_ant)
            auxiliar2 = self.auxiliar2(v_ant)
            auxiliar3 = self.auxiliar3(v_ant)
            auxiliar4 = self.auxiliar4(v_ant)

            # Eqaução T8
            estados[i*2] = v_ant + (self.delta_t/6)*(auxiliar1[0] + 2*auxiliar2[0] + 2*auxiliar3[0] + auxiliar4[0])
            estados[(i*2)+1] = y_ant + (self.delta_t/6)*(auxiliar1[1] + 2*auxiliar2[1] + 2*auxiliar3[1] + auxiliar4[1])

            v_ant = estados[i*2]
            y_ant = estados[(i*2)+1]
            
            i = i + 1

        return estados