semana=[]


for i in range(1,6):
        x=input("Insira o dia da semana: ")
        if x=="Domingo" or x=="Sábado":
            print(f"{x} não é dia útil.")
        else:    
            semana.append(x+"-feira")
print(semana)