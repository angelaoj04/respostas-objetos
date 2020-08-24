class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, QuantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__QuantidadeCombustivel = QuantidadeCombustivel

    def abastecerPorValor(self, valor):
        quantidadeLitros = valor // self.__valorLitro
        self.alterarQuantidadeCombustivel(quantidadeLitros)
        return float(quantidadeLitros)

    def abastecerPorLitro(self, litros):
        valorPagar = litros // self.__valorLitro
        self.alterarQuantidadeCombustivel(litros)
        return valorPagar

    def alteraValor(self, valor):
        if(valor > 0):
            self.__valorLitro = valor;

    def alterarCombustivel(self, combustivel):
        self.__tipoCombustivel = combustivel

    def alterarQuantidadeCombustivel(self, quantidade):
        if(quantidade <= self.__QuantidadeCombustivel):
            self.__QuantidadeCombustivel = self.__QuantidadeCombustivel - quantidade
            return True
        else:
            return False

    def retornarBomba(self):
        bomba = f'Combustível: {self.__tipoCombustivel} | Valor: R${self.__valorLitro} | Quantidade em Bomba: {self.__QuantidadeCombustivel} litros'
        return bomba

bomba = bombaCombustivel("gasolina", 4.99, 150)
print(bomba.retornarBomba())
bomba.abastecerPorLitro(10)
print(bomba.retornarBomba())
bomba.abastecerPorValor(55.00)
print(bomba.retornarBomba())