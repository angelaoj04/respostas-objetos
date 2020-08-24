class BixinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, nome):
        self.nome = nome

    def alterarFome(self, fome):
        self.fome = fome

    def alterarSaude(self, saude):
        self.saude = saude

    def alterarIdade(self, idade):
        self.idade = idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):

        if self.fome == True:
            return "está com fome"
        else:
            return "não está com fome"
        return self.fome

    def retornarSaude(self):
        if self.saude == True:
            return "Boa"
        else:
            return "Ruim"

    def retornarIdade(self):
        return self.idade

    def Humor(self):
        if(self.saude == True and self.fome == False):
            humor = "Bom"
        else:
            humor = "Ruim"
        return humor

bixinho = BixinhoVirtual("Tamagushi", False, True, 1)

bixinho.alterarFome(True)

print(f'O bixinho {bixinho.retornarNome()} tem {bixinho.retornarIdade()} ano(s), está com a saúde {bixinho.retornarSaude()} e {bixinho.retornarFome()}')
print(f'O humor do {bixinho.retornarNome()} está {bixinho.Humor()}')