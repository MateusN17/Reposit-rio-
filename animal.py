class Animal:
    def __init__(self,nome):
        self.nome=nome
    def fazer_som(self):
        print(f"O animal de nome '{self.nome}' faz algum som.")
class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.raça = raça
    def nomeeraca(self):
        print(f"O nome do cachorro é {self.nome}, da raça {self.raça}.")
    def fazer_som(self):
        print("O cachorro faz au au!")
        
animal_generico=Animal(input("Digite o nome de um animal: "))

cachorro1=Cachorro(nome=input("Insira o nome do cachorro: "),raça=input("Insira a raça do cachorro: "))
animal_generico.fazer_som() #Saída: O animal faz algum som.
cachorro1.fazer_som() #Saída: O cachorro faz au au!
cachorro1.nomeeraca()