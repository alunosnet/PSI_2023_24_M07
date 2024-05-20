"""Pretende-se um programa para gerir uma frota automóvel de uma empresa"""
import pickle,os

NOME_FICHEIRO="dados.dat"

FICHEIRO_AVARIAS="avarias.dat"

def listar_avarias():
    if os.path.exists(FICHEIRO_AVARIAS)==False:
        print("Não existem avarias")
        return
    with open(FICHEIRO_AVARIAS,"rb") as f_avarias:
        while True:
            try:
                avaria=pickle.load(f_avarias)
                #procurar o veículo ao ficheiro
                with open(NOME_FICHEIRO,"rb") as f_carros:
                    while True:
                        try:
                            carro=pickle.load(f_carros)
                            if carro['matricula']==avaria['matricula']:
                                break
                        except EOFError:
                            break
                print(f"{avaria['matricula']} \t {carro['marca']} \t {carro['modelo']} \t {carro['ano']} \t {avaria['descricao']} \t {avaria['data']} \t {avaria['custo']}")
            except EOFError:
                break

def adicionar_avaria():
    if os.path.exists(NOME_FICHEIRO)==False:
        return
    matricula=input("Matricula do veículo:")
    #verificar se matricula existe
    contar = 0
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                dados=pickle.load(ficheiro)
                if matricula==dados['matricula']:
                    contar = 1
                    break
            except EOFError:
                break
    if contar==0:
        print("Não existe nenhum veículo com a matricula indicada")
        return
    data=input("Data da avaria:")
    descricao=input("Descrição da avaria:")
    custo=int(input("Custo da avaria:"))
    novo={
        'matricula':matricula,
        'data':data,
        'descricao':descricao,
        'custo':custo
    }
    #adicionar ao ficheiro das avarias
    try:
        with open(FICHEIRO_AVARIAS,"ab") as ficheiro:
            pickle.dump(novo,ficheiro)
    except Exception as e:
        print(f"Ocorreu o seguinte erro {e}")
        return
    print("Dados registados com sucesso.")

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
        op=int(input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Remover\n5.Mais de 10 anos\n6.Marca com mais veículos\n7.Adicionar Avaria\n8.Listar Avarias\n9.Terminar"))
        if op==9:
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
        if op==7:
            adicionar_avaria()
        if op==8:
            listar_avarias()

if __name__=="__main__":
    main()