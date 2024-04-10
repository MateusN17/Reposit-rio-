from classes import Pessoa

if __name__=="__main__":
    pessoa1=Pessoa(nome=input("Insira seu nome completo: "),sexo=input("Insira como você se identifica: "), cpf=input("Insira o seu CPF: "))
    

pessoa1.dizer_olá()
pessoa1.beber()