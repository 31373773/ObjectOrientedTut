class cake:
    def __init__(self, bakery, flavor):
        self.bakery = bakery
        self.__flavor = flavor

    def display(self):
        print(self.bakery)
        print(self.__flavor)

    def getflavor(self):
        print(self.__Bakery)

    def setflavor(self, flavor):
        self.__flavor = flavor

cake = cake('Carlos Bakery', 'chocolate')
cake.display()
cake.getflavor('strawberry')
cake.setflavor()
