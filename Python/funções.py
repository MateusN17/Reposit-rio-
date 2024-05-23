def adição(qntd):
    soma= sum(qntd)
    return soma

def multiplicar (qntd):
    m=1
    for i in qntd:
        m=m*i
    return m

def divisão (qntd):
    d=qntd[0]
    for i in qntd[1:]:
        if i==0:
            return 'Erro! Não é possível dividir por 0.'
        elif i!=0:
            d=d/i
    return d

def subtração(qntd):
    s=qntd[0]-sum(qntd[1:])
    return s

def quantidade():
    numeros=[]
    quantos=int(input("Insira quantos números você quer operar: "))
    for i in range(quantos):
        numero=float(input("Digite o {}º número: ".format(i+1)))
        numeros.append(numero)
    return numeros