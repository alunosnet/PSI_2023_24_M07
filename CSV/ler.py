import csv

with open("dados.csv","r",encoding="utf-8") as ficheiro:
        leitor = csv.DictReader(ficheiro)

        for dados in leitor:
                print(dados)
                #print(dados['nome'])