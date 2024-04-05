from vendedor import Vendedor
vendedor=Vendedor(nome=input("Insira o nome do vendedor: "), vendas=int(input("Insira a quantidade de vendas: ")), meta = int(input("Insira a meta de vendas: ")))
vendedor.bateu_meta()