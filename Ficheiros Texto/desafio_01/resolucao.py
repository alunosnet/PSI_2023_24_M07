"""Programa para gerir tarefas: Adicionar, listar, remover e marcar concluída"""
import utils, os

NOME_FICHEIRO = "tarefas.txt"

def adicionar():
    tarefa=utils.le_texto("Tarefa:")
    data=utils.le_texto("Data (dd-mm-aaaa):")
    with open(NOME_FICHEIRO,"a",encoding="utf-8") as ficheiro:
        ficheiro.write(f"{tarefa},{data}\n")
    print("Tarefa registada com sucesso")

def listar():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem tarefas")
        return
    l = 1
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        #vesão 2
        #linhas=ficheiro.readlines()
        #for i,linha in enumerate(linhas,1):
            #print(f"{i} - {linha}",end="")
        while True:
            linha = ficheiro.readline()
            if not linha:
                break
            print(f"{l} - {linha}",end="")
            l += 1

def remover():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem tarefas")
        return
    numero = utils.le_numero("Qual o nº da tarefa a remover:")
    numero -= 1
    #ler todas as tarefas para uma lista
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
    #guardar novamente no ficheiro as restantes tarefas
    with open(NOME_FICHEIRO,"w",encoding="utf-8") as ficheiro:
        for i in range(len(linhas)):
            if i!=numero:
                ficheiro.write(linhas[i])
    print("Tarefa removida com sucesso!")

def marcar():
    pass

def main():
    while True:
        op=utils.menu("Menu",["Adicionar","Listar","Remover","Marcar Concluída","Terminar"])
        if op==1:
            adicionar()
        elif op==2:
            listar()
        elif op==3:
            remover()
        elif op==4:
            marcar()
        elif op==5:
            break

if __name__=="__main__":
    main()