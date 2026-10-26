#A Classe: O modelo(a planta)

class Celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar")
        else:
            self.ligado = True
            print(f" {self.modelo} ligado!")

#Os objetos criados a partir da classe Celular()
celular1 = Celular("Xiaomi", "Redmi Note 15", "Preto")
celular2 = Celular("Samsung", "Galaxy S23", "Cinza")

#Acessando e alterando os atributos
#Acessando:
print(celular2.marca)

#Alterando:
celular1.cor = "Vermelho"
print(celular1.cor)

#Chamando métodos

celular1.ligar()
celular2.ligar()
