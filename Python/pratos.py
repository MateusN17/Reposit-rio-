a=int(input("Informe a quantidade de pratos existente: ")) 

lista=list(range(1,a+1)) 

 
 

while True: 

    print("\nFila de pratos atual: ", lista) 

    print(f"Existem {len(lista)} pratos na lista.") 

    print("Digite alguma das letras de comando:") 

    print("E para empilhar um novo prato.") 

    print("D para desempilhar um prato.") 

    print("S para sair.") 

    razão=input("Insira aqui qual comando você deseja: ") 

    if razão=="E": 

        a+=1 

        lista.append(a) 

    elif razão=="D": 

        if (len(lista))>0: 

            #a-=1 

            atendido=lista.pop(-1) 

            print("Prato", atendido, "foi limpo.") 

        else: 

            print("Fila vazia. Nenhum prato para lavar.") 

    elif razão=="S": 

        print("Programa encerrado.") 

        break 

    else: 

        print("Insira uma operação válida.") 