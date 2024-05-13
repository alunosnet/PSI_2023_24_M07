"""Programa para gravar várias strings num ficheiro binário"""
import struct

quantas=int(input("Quantas strings:"))

with open("strings.dat","wb") as ficheiro:
    for i in range(quantas):
        texto=input("Insira um texto:")
        dados = struct.pack("100s",texto.encode('utf-8'))
        ficheiro.write(dados)
