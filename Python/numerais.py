print("Programa que mostra relações entre numerais (inteiros e decimais).\n")
A=int(input("Insira o 1° número (Inteiro): "))
B=int(input("Insira o 2° número (Inteiro): "))
C=float(input("Insira o 3° número (Decimal): "))

R1=(2*A)*(B/2)
R2=(3*A)+C
R3=C**3

teste=input("Escreva qual relação você deseja obter (R1,R2,R3): ")

if teste=="R1":
    print("A primeira relação é o produto do dobro do primeiro com a metade do segundo: {}".format(R1))
elif teste=="R2":
    print("A segunda relação é a soma do triplo do primeiro com o terceiro: {}".format(R2))
elif teste=="R3":
    print("A terceira relação é o terceiro número elevado ao cubo: {}".format(R3))
else:
     print("Insira uma relação válida. r1,r2,r3")
#print("A primeira relação é o produto do dobro do primeiro com a metade do segundo: {}".format(r1))
#print("A segunda relação é a soma do triplo do primeiro com o terceiro: {}".format(r2))
#print("A terceira relação é o terceiro número elevado ao cubo: {}".format(r3))