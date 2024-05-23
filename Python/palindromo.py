p=input("Insira uma palavra: ")

if p==p[::-1]:
    print("Sim, {} é um palíndromo.".format(p))
else:
    print("{} não é um palíndromo.".format(p))