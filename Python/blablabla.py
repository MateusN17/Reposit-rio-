x=input("Insira o seu nome: ")
y=input("Insira a sua idade: ")
peso=float(input("Insira o seu peso em kg: "))
altura=float(input("Informe a sua altura em m: "))

imc= peso/altura**2

import os
os.system('cls')
if imc<17:
    p="Muito abaixo do peso."
elif 17<imc<=18.5:
    p="Abaixo do peso."
elif 18.6<=imc<25:
    p="Peso ideal."
elif 25<=imc<30:
    p="Levemente acima do peso."
elif 30<=imc<35:
    p="Obesidade grau 1."
elif 35<=imc<40:
    p="Obesidade grau 2 (Severa)."
else:
    p="Obesidade grau 3 (Mórbida)."

print("Olá {}! \nSeja muito bem vindo!!! \nVocê tem {} anos. \nSua altura é {}. \nSeu Peso é {}. \nBaseado no seu índice de massa corporal: {} \nVocê está com {}".format(x,y,altura,peso,imc,p))