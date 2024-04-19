class Veículo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def escolha(self):
        print(f"A escolha do veículo foi da marca {self.marca} e de modelo {self.modelo}.")
    def frear(self):
        print(f"O veículo freou.")
    def acelerar(self):
        print(f"O veículo está acelerando.")
class Carro(Veículo):
    def __init__(self, cor, marca, modelo):
        self.cor=cor
        super().__init__(marca,modelo)
    def abrir_porta(self):
        print(f"A porta do {self.modelo},está aberta.")
    def escolha(self):
        print(f"A escolha do Carro foi da marca {self.marca} e de modelo {self.modelo}.")
class Moto(Veículo):
    def __init__(self, marca, modelo,cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada=cilindrada
    def empinar(self):
        print(f"A moto {self.marca} está empinando.")
    def escolha(self):
        print(f"A escolha da Moto foi da marca {self.marca}, com {self.cilindrada} e de modelo {self.modelo}.")
escolha=input("Escolha para ver os resultados entre (Automóveis, Carro e Moto): ")
if escolha=="Automóveis" or escolha=="automóveis":
    veiculo_generico=Veículo(marca=input("Insira a marca do veículo: "),modelo=input("Insira o modelo: "))
    import os
    os.system('cls')
    veiculo_generico.escolha()
    veiculo_generico.acelerar()
    veiculo_generico.frear()
elif escolha=="Carro" or escolha=="carro":
    carro1=Carro(marca=input("Insira a marca do carro: "), modelo=input("Insira o modelo do carro: "), cor=input("Insira a cor do carro: "))
    import os
    os.system('cls')
    carro1.escolha()
    carro1.abrir_porta()
    carro1.acelerar()
    carro1.frear()
elif escolha=="Moto" or escolha=="moto":
    moto1=Moto(marca=input("Insira a marca da moto: "), modelo=input("Insira o modelo da moto: "), cilindrada=input("Insira a cilindrada da moto: "))
    import os
    os.system('cls')
    moto1.escolha()
    moto1.acelerar()
    moto1.empinar()
    moto1.frear()
else:
    print("Insira entre automóveis, carro e moto.")