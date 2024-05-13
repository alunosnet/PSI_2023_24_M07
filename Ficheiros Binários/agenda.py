"""Um programa para gerir uma agenda de contactos com um ficheiro binários
    Funcionalidades:
        - Adicionar um contacto
        - Editar
        - Remover
        - Listar
    Dados:
        Nome [100] Idade [4] Email [64] Telefone [9]
"""
import struct

nome_ficheiro="agenda.dat"

def adicionar():
    nome=input("Nome:")
    idade=int(input("Idade:"))
    email=input("Email:")
    telefone=input("Telefone:")
    with open(nome_ficheiro,"ab") as ficheiro:
        nome=struct.pack("100s",nome.encode("utf-8"))
        ficheiro.write(nome)
        idade=struct.pack("i",idade)
        ficheiro.write(idade)
        email=struct.pack("64s",email.encode("utf-8"))
        ficheiro.write(email)
        telefone=struct.pack("9s",telefone.encode("utf-8"))
        ficheiro.write(telefone)
    print("Contacto adicionado com sucesso.")


def editar():
    pass

def remover():
    pass

def listar():
    pass

def main():
    while True:
        opcoes=["Adicionar","Editar","Remover","Listar","Sair"]
        for i, opcao in enumerate(opcoes,1):
            print(f"{i} - {opcao}")
        op=int(input("Opção:"))
        if op==len(opcoes):
            break
        elif op==1:
            adicionar()
        elif op==2:
            editar()
        elif op==3:
            remover()
        elif op==4:
            listar()

if __name__=="__main__":
    main()
