import os
from lexico import analisador_lexico
from sintatico import Sintatico
from tabelaSimbolos import TabelaDeSimbolos 

arquivo = open("codigo_fonte.txt", "r")
codigo = arquivo.read()
arquivo.close()

tabela_simbolos = TabelaDeSimbolos()

lexico = analisador_lexico(codigo)

tabela_simbolos.tabelaSimbolos()

# Cria um arquivo com os tokens
diretorio_arquivo = os.path.dirname(os.path.realpath(__file__))
os.chdir(diretorio_arquivo)

arquivo_tokens = "tokens.txt"

with open(arquivo_tokens, 'w') as arquivo:
    for token in lexico:
        arquivo.write(f"{token[0]}: {token[1]}\n")

sintatico = Sintatico(iter(lexico), tabela_simbolos)
sintatico.programa()
tabela_simbolos.imprimir_tabela()
