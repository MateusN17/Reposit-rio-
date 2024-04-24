def mdc(a,b):
    while b!=0:
        a,b=b,a%b
    return a
n1=int(input("Insira o primeiro número: "))
n2=int(input("Insira o segundo número: "))
resultado=mdc(n1,n2)
print("O MDC de {} e {} é: {}.".format(n1,n2,resultado))