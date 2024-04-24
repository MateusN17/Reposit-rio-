def media(a,b,c):
    return (a+b+c)/3

print(media(1,2,3))
print(media(3,4,5))

def melhores_alunos(alun1,alun2,alun3):
    print(f"Os melhores alunos do SESI, são: {alun1}, {alun2} e {alun3}.")
    return(alun1,alun2,alun3)

melhores_alunos("Amanda","Maria","Merlyn")

def cad_pessoa(nome,idade, endereço):
    pessoa=nome, idade, endereço
    return pessoa

nome=input("Insira o seu nome: ")
idade=int(input("Insira a sua idade: "))
endereço=input("Insira o seu endereço: ")

pessoa_cadastrada=cad_pessoa(nome,idade,endereço)