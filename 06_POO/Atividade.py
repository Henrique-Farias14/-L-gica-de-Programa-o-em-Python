class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au au!")

    def mostrar_info(self):
        print(f"{self.nome}, {self.raca}, {self.idade}")

cachorro1 = Cachorro("Pipoca", "SRD", 6)
cachorro2 = Cachorro("Pepe", "Labrador", 5)

cachorro1.mostrar_info()
cachorro2.mostrar_info()
cachorro1.latir()
cachorro2.latir()

cachorro2.idade = 7
cachorro2.mostrar_info()