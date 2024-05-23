print("Calculadora de Juros Compostos.")

C=float(input("Insira o capital inicial: "))
i=float(input("Insira a taxa de juros: "))
t=int(input("Insira a quantidade de meses: "))

M=C*(1+i/100)**t

print("O montante acumulado do capital inicial de R${}, depois de {} meses \ncom a taxa de juros de {}%, é de R${}".format(C,t,i,M))