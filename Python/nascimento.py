while True:
    x=int(input("Insira a sua idade para saber se é criança, adolescnte ou adulto: "))
    if x<=12:
        print("Você é uma criança.")
    elif x<=17:
        print("Você é um adolescente.")
    elif x>=18:
        print("Você é um adulto.")
    else: 
        print("Insira uma idade correspondente a estas classificações.")