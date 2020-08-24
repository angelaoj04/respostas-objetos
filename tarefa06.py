class tv:
    def __init__(self, canal=11, volume=11):
        self.__canal = canal
        self.__volume = volume

    def maisvol(self):
        self.__volume += 1
        if self.__volume > 99:
            self.__volume = 99

    def menosvol(self):
        self.__volume -= 1
        if self.__volume < 0:
            self.__volume = 0

    def mudacanal(self, canal):
        if canal > 0 and canal < 500:
            self.__canal = canal

    def mostra(self):
        return self.__canal, self.__volume

    def __str__(self):
        return f'TV Canal:{self.__canal} Volume:{self.__volume}'

novaTV = tv()

novaTV.maisvol()
novaTV.mudacanal(26)


print(novaTV)