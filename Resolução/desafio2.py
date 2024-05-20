"""Pretende-se um programa para gerir uma frota automóvel de uma empresa"""
import pickle,os

NOME_FICHEIRO="dados.dat"

def adicionar():
    matricula=input("Matricula:")
    marca = input("Marca:")
    modelo = input("Modelo:")
    ano = int(input("Ano de fabrico:"))
    #guardar no ficheiro binário
    with open(NOME_FICHEIRO,"ab") as ficheiro:
        novo={
            'matricula':matricula,
            'marca':marca,
            'modelo':modelo,
            'ano':ano
        }
        pickle.dump(novo,ficheiro)
    print("Dados foram guardados com sucesso.")

def listar():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veículos.")
        return
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                print(veiculo)
            except EOFError:
                break

def pesquisar():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veículos.")
        return
    marca=input("Qual a marca a pesquisar:")
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                if marca==veiculo['marca']:
                    print(veiculo)
            except EOFError:
                break

def remover():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veículos.")
        return
    matricula=input("Qual a matricula a remover:")
    contar = 0
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        with open("TEMP.DAT","wb") as ficheiro_escrita:
            while True:
                try:
                    veiculo=pickle.load(ficheiro)
                    if matricula==veiculo['matricula']:
                        contar += 1
                    else:
                        pickle.dump(veiculo,ficheiro_escrita)
                except EOFError:
                    break
    print(f"Foram removidos {contar} veículos")
    os.remove(NOME_FICHEIRO)
    os.rename("TEMP.DAT",NOME_FICHEIRO)

def extra_mais_10_anos():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veículos.")
        return
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                if 2024-veiculo['ano']>10:
                    print(veiculo)
            except EOFError:
                break

def extra_contar_marcas():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veículos.")
        return
    marcas = {}
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                if veiculo['marca'] in marcas:
                    marcas[veiculo['marca']] += 1
                else:
                    marcas[veiculo['marca']] = 1
            except EOFError:
                break
    marca_mais = ""
    maior = 0
    for marca, contagem in marcas.items():
        if contagem > maior:
            maior = contagem
            marca_mais=marca
    print(f"A marca com mais veiculos é {marca_mais} com {maior} veículos")

def main():
    while True:
        op=int(input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Remover\n5.Mais de 10 anos\n6.Marca com mais veículos\n7.Terminar"))
        if op==7:
            break
        if op==1:
            adicionar()
        if op ==2:
            listar()
        if op==3:
            pesquisar()
        if op==4:
            remover()
        if op==5:
            extra_mais_10_anos()
        if op==6:
            extra_contar_marcas()

if __name__=="__main__":
    main()