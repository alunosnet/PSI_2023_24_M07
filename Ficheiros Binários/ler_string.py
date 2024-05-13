"""Programa que lê uma string de um ficheiro binário"""
import struct

with open('string.dat','rb') as ficheiro:
    dados=ficheiro.read(100)
    texto=struct.unpack('100s',dados)[0]
    texto_limpo=texto.decode('utf-8').rstrip('\x00')

print(texto_limpo)