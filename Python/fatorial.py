def  teste():
    numero = int(input("Fatorial de: ") )
    resultado=1
    count=1

    while count <= numero:
        resultado *= count
        count += 1

    print("O fatorial de {} é {}.".format(numero,resultado))

teste()