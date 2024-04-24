def primo(numero):
    if numero<=1:
        return False
    elif numero<=3:
        return True
    elif numero%2==0 or numero%3==0:
        return False
    i=5
    while i*i<=numero:
        if numero%i==0 or numero%(i+2)==0:
            return False
        i+=6
    return True
num=int(input("Digite um número inteiro: "))
if primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")