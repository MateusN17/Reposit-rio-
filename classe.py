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
# Instancia de um objeto da classe "Aluno"
aluno=Aluno(nome=input("Insira seu nome completo: "), idade=input("Digite a sua idade: "),sexo=input("Insira como você se identifica: "), matricula=input("Insira a sua matrícula: "))
x=input("Insira o curso que você cursa: ")
y=input("Insira qual o valor que você idealiza para ganhar: ")
#Apaga o terminal
import os
os.system('cls')
#Chama os métodos de "Aluno"
aluno.dizer_olá()
aluno.curso(x)
aluno.salário(y)