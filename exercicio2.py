"""Programa para ler o ficheiro"""
import os

if os.path.exists("nomes.txt"):
    with open("nomes.txt","r",encoding='utf-8') as ficheiro:
        nomes=ficheiro.read()
        print(nomes)
else:
    print("Ficheiro com os nomes não existe")