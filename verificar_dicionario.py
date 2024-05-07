"""Programa para ler uma frase em inglês e verificar
cada palavra da frase se existe no dicionário que
está no ficheiro words.txt"""
import os

def main():
    dicionario="words.txt"
    if os.path.exists(dicionario)==False:
        print("O dicionário não existe.")
        return
    
    #ler frase do utilizador
    frase = input("Escreva uma frase em inglês:")
    #verificar se está preenchida
    if not frase or frase.strip()=="":
        print("Tem de escrever uma frase")
        return
    #converter a frase numa lista de palavras
    palavras=frase.lower().split(' ')
    #TODO: limpar as palavras de carateres de pontuação
    p_dicionario=[]
    #abrir o ficheiro
    with open(dicionario,"r",encoding='utf-8') as ficheiro:
        #ler as palavras do ficheiro para uma lista
        while True:
            linha = ficheiro.readline()
            if not linha:
                break
            p_dicionario.append(linha.strip().lower())
    #ciclo para percorrer a lista das palavras do utilizador
    for palavra in palavras:
        #verificar se cada uma existe na lista do ficheiro
        if palavra not in p_dicionario:
            print(f"A palavra:{palavra} não existe no dicionário")
            break
    #se alguma não existir dar erro, mostra qual a palavra errada e continua para as seguintes
    #TODO: falta dar uma mensagem a dizer que não há erros!
    
if __name__=="__main__":
    main()