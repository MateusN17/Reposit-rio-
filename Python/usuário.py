def solicitar_usuario():
    return input("Insira o seu usuário: ") 

def solicitar_senha():
    return input("Digite sua senha: ")

def confirmar_senha():
    return input("Confirme sua senha: ")

def main():
    usuario=solicitar_usuario()
    senha = solicitar_senha()
    confirmacao = confirmar_senha()
    tentativas_restantes = 3

    while senha != confirmacao:
        if tentativas_restantes == 0:
            print("Você excedeu o número máximo de tentativas.")
            return
        else:
            print("As senhas não coincidem. Tente novamente.")
            tentativas_restantes -= 1
            print(f"Tentativas restantes: {tentativas_restantes}")
            senha = solicitar_senha()
            confirmacao = confirmar_senha()

    print("Senha confirmada com sucesso!")

if __name__ == "__main__":
    main()