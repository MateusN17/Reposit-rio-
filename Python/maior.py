def encontrar_maior(lista):
    if len(lista) == 0:
        return None
    else:
        maior = lista[0]
        for elemento in lista:
            if elemento > maior:
                maior = elemento
        return maior
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
    print("O maior elemento na lista é:", encontrar_maior(lista))
