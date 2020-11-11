from PIL import Image

class Imagem:
    
    def __init__(self, img):
        self.img = Image.open(img).convert('F')
        self.img_orig = self.img.copy()
        self.img_final = Image.new('F',(self.img.size))
        self.larg_final, self.alt_final = self.img_final.size
        self.img_pix = self.img_final.load()
        self.pix = None

    
    def ampliar(self):
        largura, altura = self.img.size
        self.img = self.img.resize((largura+2, altura+2))
        largura = largura + 2
        altura = altura + 2
        self.pix = self.img.load()
                
        # tornar os pixels da borda da imagem com intensidade de cor 0(preto)
        for i in range(largura):
            self.pix[i,0] = 0
        
        for i in range(largura):
            self.pix[i,altura-1] = 0
        
        for i in range(altura):
            self.pix[0,i] = 0
        
        for i in range(altura):
            self.pix[largura-1,i] = 0

        # corrigir possíveis alterações indevidas
        img2 = self.img_orig.load()
        for i in range(self.larg_final):
            for k in range(self.alt_final):
                if img2[i,k] != self.pix[i+1,k+1]:
                    self.pix[i+1,k+1] = img2[i,k]


    def detector_bordas(self):
        larg, alt = self.img_final.size
        for i in range(1, self.larg_final):
            for j in range(1, self.alt_final):
                self.img_pix[i-1,j-1] = abs((self.pix[i+1,j] + self.pix[i,j-1]) - 
                                            - (self.pix[i-1,j] + self.pix[i,j+1]))


    def box_blurring(self):
        for i in range(1, self.larg_final):
            for j in range(1, self.alt_final):
                self.img_pix[i-1,j-1] = (self.pix[i+1,j] + self.pix[i,j+1] + 
                                        + self.pix[i-1,j] + self.pix[i,j-1])/4


    def gaussian_blur(self):
        for i in range(1, self.larg_final):
            for j in range(1, self.alt_final):
                self.img_pix[i-1,j-1] = ((2*(self.pix[i+1,j] + self.pix[i,j+1] + self.pix[i-1,j] + 
                                         + self.pix[i,j-1] + (2*(self.pix[i,j])))) + self.pix[i-1,j-1] +
                                         + self.pix[i+1,j+1] + self.pix[i+1,j-1] + self.pix[i-1,j+1])/16


    def exibir_imagens(self):
        self.img_orig.show() # imagem por baixo
        self.img_final.show() # imagem por cima