"""Programa para gravar uma string num ficheiro binário"""
import struct

texto=input("Insira um texto:")

with open("string.dat","wb") as ficheiro:
    dados = struct.pack("100s",texto.encode('utf-8'))
    ficheiro.write(dados)
