"""Programa para gravar vários inteiros num ficheiro binário"""
import struct

quantos=int(input("Quantos inteiros pretende gravar:"))

#abrir o ficheiro para gravar o numero
with open("inteiros.dat","wb") as ficheiro:
    for i in range(quantos):
        numero = int(input("Insira um nº:"))
        temp=struct.pack("i",numero)
        ficheiro.write(temp)

