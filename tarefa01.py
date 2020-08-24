class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print("A cor da Bola é:", self.cor)

bola1 = Bola("branca", "50", "plástico")
bola1.mostraCor()
bola1.trocaCor("vermelha")
bola1.mostraCor()
