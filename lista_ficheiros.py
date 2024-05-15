import os

def listar_ficheiros(caminho):
    #listar os ficheiros e as pastas da pasta atual
    ficheiros = os.listdir(caminho)
    #listar todos
    print(ficheiros)
    #entrar nas pastas
    for ficheiro in ficheiros:
        if not os.path.isfile(os.path.join(caminho,ficheiro)):
            listar_ficheiros(os.path.join(caminho,ficheiro))

listar_ficheiros(".")