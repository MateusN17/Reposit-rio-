a=input("Você está negativado: ")
b=input("Você está empregado: ")
c=input("Tem salário: ")
d=input("Casa própria: ")
e=float(input("Valor do salário: "))    
 
if a=="Sim" or a=="sim":
    print("Negado.")
    
elif b=="Não" or b=="Não":
    print("Negado.")
elif c=="Não" or c=="Não":
    print("Negado.")
elif d=="Não" or d=="não":
    print("Negado.")
        
else:
    e=e*1.5
    print("Seu valor de empréstimo é de {}.".format(e))