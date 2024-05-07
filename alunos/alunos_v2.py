"""
Programa para guardar dados de vários alunos em um ficheiro de texto
Neste projeto os dados estão todos só no ficheiro e são lidos/escritos quando é necessário
"""
import utils


#nome do ficheiro
nome_ficheiro = "alunos.txt"

def criar_aluno():
    """Função para ler os seguintes dados:
    Nome, morada, email e idade de um aluno
    Devolve um dicionário com os dados"""
    pass

def listar():
    """Função para listar os alunos do ficheiro"""
    pass

def adicionar():
    """Função para adicionar um aluno ao ficheiro"""
    pass


def main():
    while True:
        op=utils.menu("Ficheiros Texto",["Adicionar","Listar","Terminar"])
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            break

if __name__=="__main__":
    main()