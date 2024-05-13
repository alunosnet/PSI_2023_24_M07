"""Programa para adicionar texto a um ficheiro"""
with open("meu_ficheiro.txt","a",encoding='utf-8') as ficheiro:
    ficheiro.write("Olá mundo\n")
