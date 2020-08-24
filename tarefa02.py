class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarValorlado(self, lado):
        self.lado = lado

    def retornarValorlado(self):
        return self.lado

    def calcularArea(self):
        area = self.lado * self.lado
        return area

quadrado1 = Quadrado(50)
print(quadrado1.lado)

print("O valor da área do quadrado é: ",quadrado1.calcularArea())
print("O valor do lado do quadrado é: ",quadrado1.retornarValorlado())
