class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def crescer(self, altura):
        self.__altura += altura
        return self.__altura

    def envelhecer(self, anos):
        idadeAntes = self.__idade
        self.__idade += anos
        if (idadeAntes < 21):
            self.crescer(anos * 0.05)
        else:
            self.crescer((21 - idadeAntes) * 0.05)
        return self.__idade

    def engordar(self, kilos):
        self.__peso += kilos
        return self.__peso

    def emagrecer(self, kilos):
        self.__peso -= kilos
        return self.__peso

ana = Pessoa("Ana", 30, 65, 165)

print(ana.envelhecer(2))
print(ana.crescer(0))
print(ana.engordar(2))

