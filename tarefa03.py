
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarValorLados(self, novoComprimento, novalargura):
        self.comprimento = novoComprimento
        self.largura = novalargura

    def calcularArea(self):
        area = self.comprimento * self.largura
        return area

    def calcularPerimetro(self):
        perimetro = (self.comprimento + self.largura)*2
        return perimetro

print("Informe as medidas de um local")

comprimento = float(input("Informe o valor do comprimento do local: "))
largura = float(input("Informe o valor da largura do local: "))

local = Retangulo(comprimento, largura)
print(f'Área: {local.calcularArea()}')
print(f'Perímetro: {local.calcularPerimetro()}')

print(f'Para revestir o local informado serão necessários: {local.calcularArea()} metros quadrados de piso')



