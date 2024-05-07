"""Programa que lê um ficheiro de texto linha a linha"""
import os

if os.path.exists("meu_ficheiro.txt")==False:
    print("O ficheiro não foi encontrado")
else:
    with open("meu_ficheiro.txt","r",encoding='utf-8') as ficheiro:
        #ciclo para ler o ficheiro linha a linha
        while True:
            #ler uma linha do ficheiro
            texto = ficheiro.readline()
            #verificar se atingimos o final do ficheiro
            if not texto:
                break
            print(texto.strip())