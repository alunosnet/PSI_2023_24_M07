"""Programa para escrever num ficheiro de texto"""
with open("meu_ficheiro.txt","w",encoding='utf-8') as ficheiro:
    ficheiro.write("Olá mundo\n")
