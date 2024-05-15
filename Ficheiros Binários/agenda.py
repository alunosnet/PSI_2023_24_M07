"""Um programa para gerir uma agenda de contactos com um ficheiro binários
    Funcionalidades:
        - Adicionar um contacto
        - Editar
        - Remover
        - Listar
    Dados:
        Nome [100] Idade [4] Email [64] Telefone [9]
"""
import struct, os

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
    posicao = int(input("Qual o nº do contacto a editar:"))
    posicao = (posicao - 1) * 177
    with open(nome_ficheiro,"rb+") as ficheiro:
        ficheiro.seek(posicao)
        dados_binarios = ficheiro.read(177)
        if not dados_binarios:
            return
        nome, idade, email, telefone = struct.unpack("100si64s9s",dados_binarios)
        nome = nome.decode('utf-8').rstrip('\x00')
        email = email.decode('utf-8').rstrip('\x00')
        telefone = telefone.decode('utf-8').rstrip('\x00')
        print(f"{nome}\t{idade}\t{email}\t{telefone}")
        #novos dados do contacto
        nome=input("Nome:")
        idade=int(input("Idade:"))
        email=input("Email:")
        telefone=input("Telefone:")
        #posicionar no ficheiro
        ficheiro.seek(posicao)
        nome=struct.pack("100s",nome.encode("utf-8"))
        ficheiro.write(nome)
        idade=struct.pack("i",idade)
        ficheiro.write(idade)
        email=struct.pack("64s",email.encode("utf-8"))
        ficheiro.write(email)
        telefone=struct.pack("9s",telefone.encode("utf-8"))
        ficheiro.write(telefone)

def ficheiro_existe(nomeficheiro):
    return os.path.exists(nomeficheiro)

def remover():
    #verificar se o ficheiro existe
    if ficheiro_existe(nome_ficheiro)==False:
        print("Não tem contactos.")
        return
    posicao = int(input("Qual a posição do contacto a remover: "))
    posicao = (posicao -1) * 177
    registo = 0
    with open(nome_ficheiro,"rb") as ficheiro_leitura:
        with open("TEMP.DAT","wb") as ficheiro_escrita:
            while True:
                dados = ficheiro_leitura.read(177)
                if not dados:
                    break
                if posicao != registo:
                    ficheiro_escrita.write(dados)
                registo += 177
    os.remove(nome_ficheiro)
    os.rename("TEMP.DAT",nome_ficheiro)
    print("Contacto removido com sucesso.")

def listar():
    #verificar se o ficheiro existe
    if os.path.exists(nome_ficheiro)==False:
        print("Não tem contactos.")
        return
    op=input("Listar [T]odos ou Lista [U]m")
    with open(nome_ficheiro,"rb") as ficheiro:
        if op in "Tt":
            #listar todos
            i = 1
            while True:
                dados_binarios = ficheiro.read(177)
                if not dados_binarios:
                    break
                nome, idade, email, telefone = struct.unpack("100si64s9s",dados_binarios)
                nome = nome.decode('utf-8').rstrip('\x00')
                email = email.decode('utf-8').rstrip('\x00')
                telefone = telefone.decode('utf-8').rstrip('\x00')
                print(f"{i}\t{nome}\t{idade}\t{email}\t{telefone}")
                i += 1
        elif op in "Uu":
            #listar um contacto
            posicao = int(input("Qual o nº do contacto:"))
            posicao=(posicao-1) * 177
            ficheiro.seek(posicao)
            dados_binarios = ficheiro.read(177)
            if not dados_binarios:
                return
            nome, idade, email, telefone = struct.unpack("100si64s9s",dados_binarios)
            nome = nome.decode('utf-8').rstrip('\x00')
            email = email.decode('utf-8').rstrip('\x00')
            telefone = telefone.decode('utf-8').rstrip('\x00')
            print(f"{nome}\t{idade}\t{email}\t{telefone}")

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
