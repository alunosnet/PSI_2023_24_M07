import csv

dados = [
    {'nome':'Joaquim',
     'idade':30,
     'cidade':'Viseu'},
    {'nome':'Maria',
     'idade':25,
     'cidade':'Lisboa'},
    {'nome':'António',
     'idade':35,
     'cidade':'Tondela'}
]

with open("dados.csv","w",encoding='utf-8',newline='') as ficheiro:
    #cabeçalho
    campos = dados[0].keys()
    gravador = csv.DictWriter(ficheiro,fieldnames=campos)
    gravador.writeheader()
    for dado in dados:
        gravador.writerow(dado)
