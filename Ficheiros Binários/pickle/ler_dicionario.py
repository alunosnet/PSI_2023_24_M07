import pickle

NOME_FICHEIRO="dados.dat"

with open(NOME_FICHEIRO,"rb") as ficheiro:
    while True:
        try:
            dicionario = pickle.load(ficheiro)
            print(dicionario)
        except EOFError:
            break