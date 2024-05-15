import pickle

dicionario = {'nome':'joaquim',
              'idade':23,
              'email':'joaquim@gmail.com'}

NOME_FICHEIRO="dados.dat"

with open(NOME_FICHEIRO,"ab") as ficheiro:
    pickle.dump(dicionario,ficheiro)
