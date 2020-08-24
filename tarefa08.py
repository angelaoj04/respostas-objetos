class Macaco:
    def __init__(self, nome, bucho = ""):
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        if alimento != "":
            self.bucho = alimento


    def digerir(self):
        if(self.bucho != ""):
            self.bucho = ""
            return "Digerido!"
        else:
            return "Bucho Vazio!"

    def verBucho(self):
        print(f'Dentro do bucho do macaco {self.nome} tem {self.bucho}')

ole = Macaco("Ole")
pangole = Macaco("Pangole")

ole.comer("Folha")
ole.verBucho()
ole.comer("Banana")
ole.verBucho()
ole.comer("Ração")
ole.verBucho()
ole.digerir()
ole.verBucho()

pangole.comer("Folha")
pangole.verBucho()
pangole.comer("banana")
pangole.verBucho()
pangole.comer("farinha")
pangole.verBucho()
pangole.digerir()
pangole.verBucho()

ole.comer(pangole)
ole.verBucho()