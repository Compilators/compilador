import sys
import os
sys.path.append('../')

from lexico import analisador_lexico
from sintatico import Sintatico

arquivo = open("codigo_fonte.txt","r")
texto = arquivo.read()
arquivo.close()

lexico = analisador_lexico(texto)

# Cria um arquivo com os tokens
diretorio_arquivo = os.path.dirname(os.path.realpath(__file__))
os.chdir(diretorio_arquivo)

arquivo_tokens = "tokens.txt"

with open(arquivo_tokens, 'w') as arquivo:
    for token in lexico:
        arquivo.write(f"{token[0]}: {token[1]}\n")

sintatico = Sintatico(iter(lexico))
sintatico.programa()
