"""Programa para gravar um inteiro num ficheiro binário"""
import struct

numero = 1234

#abrir o ficheiro para gravar o numero
with open("inteiro.dat","wb") as ficheiro:
    temp=struct.pack("i",numero)
    ficheiro.write(temp)

