class Vendedor():
    def __init__(self,nome,vendas,meta):
        self.nome = nome
        self.vendas = vendas
        self.meta = meta
    def vendeu(self, vendas):
        self.vendas=vendas
    def bateu_meta(self):
        if self.vendas>=self.meta:
            print(f"{self.nome} bateu a meta.")
        else:
            print(f"{self.nome} não bateu a meta.")

#vendedor=Vendedor(nome=input("Insira o nome do vendedor: "), vendas=int(input("Insira a quantidade de vendas: ")), meta = int(input("Insira a meta de vendas: ")))
#vendedor.bateu_meta()