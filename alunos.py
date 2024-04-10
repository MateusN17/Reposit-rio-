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
