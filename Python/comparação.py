a=float(input("Insira o primeiro valor: "))
b=float(input("Insira o segundo valor: "))

if a==b:
    print("{} e {} são iguais.".format(a,b))
elif a>b:
    print("{} é maior que {}".format(a,b))
elif a<b:
    print("{} é menor que {}.".format(a,b))
else:
    print("Insira números válidos.")