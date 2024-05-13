"""
Programa para guardar dados de vários alunos em um ficheiro de texto
Neste projeto os dados estão todos só no ficheiro e são lidos/escritos quando é necessário
"""
import utils,os


#nome do ficheiro
nome_ficheiro = "alunos2.txt"

def criar_aluno():
    """Função para ler os seguintes dados:
    Nome, morada, email e idade de um aluno
    Devolve um dicionário com os dados"""
    nome = utils.le_texto("Qual o nome: ")
    morada = utils.le_texto("Qual a morada: ")
    email = utils.le_email("Qual o email: ")
    idade = utils.le_numero("Qual a idade: ")
    aluno={"nome":nome,"morada":morada,"email":email,"idade":idade}
    return aluno

def listar():
    """Função para listar os alunos do ficheiro"""
    #verificar se o ficheiro existe
    if ficheiro_existe()==False:
        return
    #abrir o ficheiro para leitura
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        while True:
            linha = ficheiro.readline()
            if not linha or len(linha)==0:
                break
            nome, morada, email, idade = linha.strip().split(",")
            print(f"{nome} - {idade} - {email} - {morada}")

def ficheiro_existe():
    if os.path.exists(nome_ficheiro)==False:
        print("Ainda não tem dados.")
        return False
    return True

def adicionar():
    """Função para adicionar um aluno ao ficheiro"""
    aluno = criar_aluno()
    #abrir o ficheiro para adicionar
    with open(nome_ficheiro,"a",encoding="utf-8") as ficheiro:
        ficheiro.write(f"{aluno['nome']},{aluno['morada']},{aluno['email']},{aluno['idade']}\n")
    print("Dados guardados com sucesso")

def apagar():
    """Função para remover um aluno do ficheiro"""
    if ficheiro_existe()==False:
        return
    nome = utils.le_texto("Nome do aluno a remover:")
    with open(nome_ficheiro,"r",encoding="utf-8") as f_leitura:
        with open("temp.txt","w",encoding="utf-8") as f_escrita:
            while True:
                linha = f_leitura.readline()
                if not linha:
                    break
                aluno = linha.split(',')
                apaguei=False
                if aluno[0] != nome or apaguei == True:
                    f_escrita.write(linha)
                else:
                    apaguei=True
    #apagar ficheiro
    os.remove(nome_ficheiro)
    #mudar o nome do ficheiro temporário
    os.rename("temp.txt",nome_ficheiro)

def pesquisar():
    #verificar se o ficheiro existe
    if ficheiro_existe()==False:
        return
    nome_pesquisar = utils.le_texto("Qual o nome a pesquisar: ")
    #abrir o ficheiro para leitura
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        while True:
            linha = ficheiro.readline()
            if not linha or len(linha)==0:
                break
            nome, morada, email, idade = linha.strip().split(",")
            if nome_pesquisar in nome:
                print(f"{nome} - {idade} - {email} - {morada}")


def main():
    while True:
        opcoes=["Adicionar","Listar","Apagar","Terminar"]
        op=utils.menu("Ficheiros Texto",opcoes)
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            apagar()
        if op==len(opcoes):
            break

if __name__=="__main__":
    main()