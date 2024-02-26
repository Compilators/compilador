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

tokens = []
with open(arquivo_tokens, 'r') as arquivo:
    for linha in arquivo:
        tipo, valor = linha.split(": ", 1)
        tokens.append({tipo: valor.strip()})

sintatico = Sintatico(iter(lexico), tabela_simbolos)
sintatico.programa()
tabela_simbolos.imprimir_tabela()

codigo_intermediario = []
codigo_tres_enderecos = []
temp_counter = 1

for token in tokens:
    for tipo, valor in token.items():
        if tipo == "ID":
            codigo_intermediario.append(f"LOAD {valor}")
        elif tipo == "NUMERO":
            codigo_intermediario.append(f"PUSH {valor}")
        elif tipo == "BOOLEANO":
            codigo_intermediario.append(f"PUSH {valor}")
        elif tipo == "STRING":
            codigo_intermediario.append(f"PUSH {valor}")
        elif tipo == "ATRIBUICAO":
            codigo_intermediario.append("STORE")
        elif tipo == "ENQUANTO":
            codigo_intermediario.append("LABEL inicio_while")
        elif tipo == "ABRE_PARENTESE":
            pass
        elif tipo == "FECHA_PARENTESE":
            pass
        elif tipo == "ABRE_CHAVE":
            pass
        elif tipo == "FECHA_CHAVE":
            pass
        elif tipo == "IMPRIMIR":
            codigo_intermediario.append("PRINT")
        elif tipo == "MAIS":
            codigo_intermediario.append("ADD")
        elif tipo == "VEZES":
            codigo_intermediario.append("MULTIPLY")
        elif tipo == "MENOR":
            codigo_intermediario.append("LESS_THAN")
        elif tipo == "IGUAL":
            codigo_intermediario.append("EQUALS")
        elif tipo == "SE":
            codigo_intermediario.append("JUMP_IF_FALSE fim_condicao")
        elif tipo == "CONTINUAR":
            codigo_intermediario.append("JUMP inicio_while")
        elif tipo == "INTERROMPER":
            codigo_intermediario.append("JUMP fim_while")

for i in range(len(codigo_intermediario)):
    if codigo_intermediario[i] == "LOAD":
        codigo_tres_enderecos.append(f"{codigo_intermediario[i+1]} = {codigo_intermediario[i+2]}")
    elif codigo_intermediario[i] == "STORE":
        codigo_tres_enderecos.append(f"{codigo_intermediario[i-1]} = t{temp_counter}")
        temp_counter += 1
    elif codigo_intermediario[i] == "ADD":
        codigo_tres_enderecos.append(f"t{temp_counter} = {codigo_intermediario[i-1]} + {codigo_intermediario[i+1]}")
        temp_counter += 1
    elif codigo_intermediario[i] == "MULTIPLY":
        codigo_tres_enderecos.append(f"t{temp_counter} = {codigo_intermediario[i-1]} * {codigo_intermediario[i+1]}")
        temp_counter += 1
    elif codigo_intermediario[i] == "LESS_THAN":
        codigo_tres_enderecos.append(f"t{temp_counter} = {codigo_intermediario[i-1]} < {codigo_intermediario[i+1]}")
        temp_counter += 1
    elif codigo_intermediario[i] == "EQUALS":
        codigo_tres_enderecos.append(f"t{temp_counter} = {codigo_intermediario[i-1]} == {codigo_intermediario[i+1]}")
        temp_counter += 1
    elif codigo_intermediario[i] == "JUMP_IF_FALSE":
        codigo_tres_enderecos.append(f"if not t{temp_counter-1} goto {codigo_intermediario[i+1]}")
    elif codigo_intermediario[i] == "JUMP":
        codigo_tres_enderecos.append(f"goto {codigo_intermediario[i+1]}")
    elif codigo_intermediario[i] == "LABEL":
        codigo_tres_enderecos.append(f"{codigo_intermediario[i+1]}:")
    elif codigo_intermediario[i] == "PRINT":
        codigo_tres_enderecos.append(f"print({codigo_intermediario[i+1]})")

codigo_intermediario.append("LABEL fim_while")

print('\n' + 'Codido de tres enderecos: ' + '\n')
print("\n".join(codigo_tres_enderecos))
