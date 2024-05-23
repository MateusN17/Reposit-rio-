import funções
qntd=funções.quantidade()
def escolha():
    while True:
        print("R1:Adição,R2:Multiplicação, R3:Divisão, R4: Subtração")
        z=input("Insira a relação desejada: ")
        
        if z =="R1" or z=="r1":
            soma=funções.adição(qntd)
            print("A soma é: {}".format(soma))    
            break 
        elif z=="R2" or z=="r2":
            multiplicação=funções.multiplicar(qntd)
            print("A multiplicação é: {}".format(multiplicação))
            break
        elif z=="R3" or z=="r3":
            divisão=funções.divisão(qntd)
            print("A divisão é: {}".format(divisão))
            break
        elif z=="R4" or z=="r4":
            sub=funções.subtração(qntd)
            print("A sub é: {}".format(sub))
            break
        else:
            print("Operação Inválida.")
while True:
    escolha()