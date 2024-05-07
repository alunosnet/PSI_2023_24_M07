"""Programa para remover os nomes repetidos do ficheiro"""
import os

nomes=[]

if os.path.exists("nomes.txt"):
    #abrir ficheiro
    with open("nomes.txt","r",encoding='utf-8') as ficheiro:
        while True:
            #ler um nome do ficheiro
            nome = ficheiro.readline()
            #verificar se chegou ao final do ficheiro
            if not nome:
                break
            #retirar o \n do final do nome
            nome = nome.strip()
            #verificar se existe na lista de nomes
            if nome in nomes:
                continue
            #se não existir adicionar à lista
            nomes.append(nome)
    #no final do ficheiro
    #guardar todos os nomes da lista no ficheiro
    #substituindo os seus dados
    with open("nomes.txt","w",encoding='utf-8') as ficheiro:
        #gravar cada um dos nomes da lista
        for nome in nomes:
            ficheiro.write(nome+"\n")
        