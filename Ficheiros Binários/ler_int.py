"""Programa para ler um inteiro de um ficheiro binário"""
import struct

with open("inteiro.dat","rb") as ficheiro:
    temp=ficheiro.read(4)
    numero=struct.unpack('i',temp)[0]

print(numero)