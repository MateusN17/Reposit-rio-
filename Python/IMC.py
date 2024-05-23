peso=float(input("Insira o seu peso em kg: "))
altura=float(input("Informe a sua altura em m: "))

imc= peso/altura**2

print("O seu imc é: ", imc)

if imc<17:
    print("Muito abaixo do peso.")
elif 17<imc<=18.5:
    print("Abaixo do peso.")
elif 18.6<=imc<25:
    print("Peso ideal.")
elif 25<=imc<30:
    print("Levemente acima do peso.")
elif 30<=imc<35:
    print("Obesidade grau 1.")
elif 35<=imc<40:
    print("Obesidade grau 2.")
else:
    print("Obesidade grau 3.")