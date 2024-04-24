def contar_vogais(palavra):
    vogais = 'aeiouAEIOU'
    quantidade = 0
    for letra in palavra:
        if letra in vogais:
            quantidade += 1
    return quantidade
palavra = input("Digite uma palavra: ")
print("A quantidade de vogais na palavra é:", contar_vogais(palavra))