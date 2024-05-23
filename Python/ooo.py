#while True:
    #nome=input("Insira o seu nome, o programa retornará \nse existe i nele: ")
    #print("i" in nome)
    #print("t" not in nome)
    
while True:
    x=input("Insira a frase: ")
    y=input("Insira sua palavra desejada: ")
    if y in x:
        print("{} está em {}".format(y,x))
    else:
        print("{} não está em {}".format(y,x))