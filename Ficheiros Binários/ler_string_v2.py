"""Programa que lê todas as strings de um ficheiro binário"""
import struct

with open('strings.dat','rb') as ficheiro:
    while True:
        dados=ficheiro.read(100)
        if not dados:
            break
        texto=struct.unpack('100s',dados)[0]
        texto_limpo=texto.decode('utf-8').rstrip('\x00')
        print(texto_limpo)
    #pedir a posição da string a ler
    posicao=int(input("Qual a string a ler:"))
    posicao = (posicao-1)*100
    ficheiro.seek(posicao)
    dados=ficheiro.read(100)
    texto=struct.unpack('100s',dados)[0]
    texto_limpo=texto.decode('utf-8').rstrip('\x00')
    print(texto_limpo)
