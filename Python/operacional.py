def quantidade():
    numeros=[]
    quantos=int(input("Insira quantos números você quer operar: "))
    for i in range(quantos):
        numero=float(input("Digite o {}º número: ".format(i+1)))
        numeros.append(numero)
    return numeros
qntd=quantidade()
so=[qntd]
print(so)
while True:
    print("1-Windows XP, 2-Unix, 3-Linux, 4-Netware, 5-Mac OS, 6-Outro")
    a=input("Insira qual o melhor sistema operacional paara uso em servidores: ")
    if a=="1":
        print("Voto validado.")
    elif a=="2":
        print("Voto validado.")
    elif a=="3":
        print("Voto validado.")
    elif a=="4":
        print("Voto validado.")
    elif a=="5":
        print("Voto validado.")
    elif a=="6":
        print("Voto validado.")
    elif a=="0":
        print("Saindo e imprimindo o valor em '%' da cada opção.")
        print()
        break
    else:
        print("Insira um valor de 0 até 6.")