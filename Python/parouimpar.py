print("Bem vindo(a) ao programa que identifica se um número é par ou ímpar.")

num=float(input("Insira o número que deseja avaliar: "))

teste=num%2
if teste==0:
    print("{} é par.".format(num))
else:
    print("{} é ímpar.".format(num))