"""Programa para ler todos os inteiros de um ficheiro binário"""
import struct

with open("inteiros.dat","rb") as ficheiro:
    while True:
        temp=ficheiro.read(4)
        if not temp:
            break
        numero=struct.unpack('i',temp)[0]
        print(numero)
    #perguntar qual o nº a ler
    posicao = int(input("Qual o nº a ler:"))
    #calcular a posição a ler sabendo que cada inteiro corresponde a 4 bytes
    posicao = (posicao-1) * 4
    ficheiro.seek(posicao)
    temp=ficheiro.read(4)
    numero=struct.unpack('i',temp)[0]
    print(numero)