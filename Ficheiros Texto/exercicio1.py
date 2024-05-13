"""Programa que lê 10 nomes e grava num ficheiro de texto"""
with open("nomes.txt","w",encoding='utf-8') as ficheiro:
    for i in range(10):
        nome=input("Introduza um nome:")
        ficheiro.write(nome+"\n")
print("Dados guardados com sucesso")