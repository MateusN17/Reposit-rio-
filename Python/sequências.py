resultado=[]
print("Insira, prometendo responder somente a verdade, com 'Sim' e 'Não': ")
t=input("Telefonou para a vítima? ").lower
e=input("Esteve no local do crime? ").lower
m=input("Mora perto da vítima? ").lower
ti=input("Tinha dívidas com a vítima? ").lower
j=input("Já trabalhou com a vítima? ").lower
resultado.append(t)
resultado.append(e)
resultado.append(m)
resultado.append(ti)
resultado.append(j)
rp=resultado.count("Sim")
rn=resultado.count("Não")

if rp==1 or rp==0:
    print("Inocente.")
elif rp==2:
    print("Suspeito.")
elif rp==3 or rp==4:
    print("Cúmplice.")
elif rp==5:
    print("Assasino.")
else:
    print("Responda, apenas, com 'Sim' ou 'Não'.")