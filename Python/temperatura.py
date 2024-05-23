print("Bem vindo(a)!!! \nEste é o programa para converter temperaturas!!!")
print("R1: Relação de graus Fahrenheit para a escala Celsius.")
print("R2: Relação de graus Celsius para a escala Fahrenheit.")
print("R3: Relação de Kelvin para graus Celsius.")
print("R4: Relação de graus Celsius para Kelvin.")
print("R5: Relação de graus Fahrenheit para Kelvin.")
print("R6: Relação de Kelvin para graus Fahrenheit.")
T=input("Insira a relação, que deseja, entre temperaturas: ")
import os
os.system('cls')
while True:
    if T=="R1":
        F=float(input("Insira a Temperatura (Fahrenheit): "))
        c=5*((F-32)/9)
        print("A temperatura de {}°F equivale a {}°C.".format(F,c))
    elif T=="R2":
        C=float(input("Insira o valor da temperatura (Celsius): "))
        F=1.8*C+32
        print("O valor de {}°C equivale a {}°F".format(C,F))
    elif T=="R3":
        K=float(input("Insira a sua temperatura na escala Kelvin: "))
        C=K-273.15
        print("A sua temperatura de {}K equivale a {}°C.".format(K,C))
    elif T=="R4":
        C=float(input("Insira a sua temperatura (Celsius): "))
        K=C+273.15
        print("A sua temperatura de {}°C equivale a {}K.".format(C,K))
    elif T=="R5":
        F=float(input("Insira a Temperatura (Fahrenheit): "))
        K=(F-32)*(5/9)+273
        print("A temperatura de {}°F equivale a {}K.".format(F,K))
    elif T=="R6":
        K=float(input("Insira a temperatura (Kelvin): "))
        F=(K-273)*1.8+32
        print("A temperatura de {}K equivale a {}°F.".format(K,F))
    else:
        print("Insira uma relação válida: R1,R2,R3,R4,R5,R6.")