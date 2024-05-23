def ordenar_crescente(lista):
    return sorted(lista)
lista = []
while True:
    numero = input("Digite um número (ou 'sair' para parar): ")
    if numero.lower() == 'sair':
        break
    try:
        numero = float(numero)
        lista.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")
if not lista:
    print("A lista está vazia.")
else:
    import os
    os.system('cls')
    print("Lista original:", lista)
    print("Lista ordenada em ordem crescente:", ordenar_crescente(lista))
