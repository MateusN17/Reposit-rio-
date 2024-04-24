x=int(input("Insira a sua data de nascimento: "))
ano=2024-x

if ano==0 or ano==1:
    print("Recém nascido, {} anos.".format(ano))
elif ano>=2 and ano<=12:
    print("Criança, {} anos.".format(ano))
elif ano>=13 and ano<=18:
    print("Adolescente, {} anos.".format(ano))
elif ano>=19 and ano<=60:
    print("Adulto, {} anos.".format(ano))
elif ano>=61 and ano<=80:
    print("Idoso, {} anos.".format(ano))
elif ano>80:
    print("Longevo, {} anos.".format(ano))
else:
    print("Insira uma data válida.")