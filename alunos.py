from classes import Aluno
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