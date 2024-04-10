class Aluno():
    def __init__ (self, nome, sexo, idade, matricula):
        self.nome=nome
        self.sexo=sexo
        self.idade=idade
        self.matricula=matricula
    def dizer_olá(self):
        print(f"Olá, meu nome é {self.nome}. Tenho {self.idade} "
              f"anos e minha matrícula é {self.matricula}. \nMe identifico como {self.sexo}.")
    def curso(self,curso:str):
        print(f"Estou cursando {curso}.")
    def salário(self,salario:float):
        print(f"Espero ganhar: R$ {salario}")

class Pessoa():
    def __init__(self,nome, sexo, cpf):
        self.nome=nome
        self.sexo=sexo
        self.cpf=cpf
    def dizer_olá(self):
        print(f"Olá, meu nome é {self.nome}."
              f" Meu cpf é: {self.cpf}. \nMe identifico como {self.sexo}.")
    def comer(self):
        return f"{self.nome} está comendo."
    def beber(self):
        return f"{self.nome} está bebendo."
    def falar(self, mensagem):
        return f"{self.nome} está falando: {mensagem}"
    def correr(self):
        return f"{self.nome} está correndo."    
class Carro:
    def __init__(self, placa, modelo, ano):
        self.placa=placa
        self.modelo=modelo
        self.ano=ano
