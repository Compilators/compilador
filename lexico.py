def analisador_lexico(codigo_fonte):
    tokens = []
    pos = 0
    length = len(codigo_fonte)

    while pos < length:
        if codigo_fonte[pos] in ' \t\n':
            pos += 1
        elif codigo_fonte[pos] == '+':
            tokens.append(('MAIS', '+'))
            pos += 1
        elif codigo_fonte[pos] == '-':
            tokens.append(('MENOS', '-'))
            pos += 1
        elif codigo_fonte[pos] == '*':
            tokens.append(('VEZES', '*'))
            pos += 1
        elif codigo_fonte[pos] == '/':
            tokens.append(('DIVIDE', '/'))
            pos += 1
        elif codigo_fonte[pos] == '=':
            tokens.append(('ATRIBUICAO', '='))
            pos += 1
        elif codigo_fonte[pos] == '!':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('DIFERENTE', '!='))
                pos += 2
            else:
                print(f"Erro: Caractere inesperado '{codigo_fonte[pos]}' na posicao {pos+1}")
                pos += 1
        elif codigo_fonte[pos] == '>':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MAIOR_IGUAL', '>='))
                pos += 2
            else:
                tokens.append(('MAIOR', '>'))
                pos += 1
        elif codigo_fonte[pos] == '<':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MENOR_IGUAL', '<='))
                pos += 2
            else:
                tokens.append(('MENOR', '<'))
                pos += 1
        elif codigo_fonte[pos] == '(':
            tokens.append(('ABRE_PARENTESE', '('))
            pos += 1
        elif codigo_fonte[pos] == ')':
            tokens.append(('FECHA_PARENTESE', ')'))
            pos += 1
        elif codigo_fonte[pos] == ',':
            tokens.append(('VIRGULA', ','))
            pos += 1
        elif codigo_fonte[pos] == ':':
            tokens.append(('DOIS_PONTOS', ':'))
            pos += 1
        elif codigo_fonte[pos] == '"':
            inicio = pos
            pos += 1
            while pos < length and codigo_fonte[pos] != '"':
                pos += 1
            if pos < length and codigo_fonte[pos] == '"':
                tokens.append(('STRING', codigo_fonte[inicio + 1:pos]))
                pos += 1
            else:
                print(f"Erro: String nao terminada, começando na posicao {inicio+1}")
        elif codigo_fonte[pos].isalpha() or codigo_fonte[pos] == '_':
            inicio = pos
            pos += 1
            while pos < length and (codigo_fonte[pos].isalnum() or codigo_fonte[pos] == '_'):
                pos += 1
            palavra = codigo_fonte[inicio:pos]
            if palavra == 'verdadeiro' or palavra == 'falso':
                tokens.append(('BOOLEANO', palavra))
            elif palavra == 'funcao':
                tokens.append(('FUNCAO', palavra))
            elif palavra == 'se':
                tokens.append(('SE', palavra))
            elif palavra == 'senao':
                tokens.append(('SENAO', palavra))
            elif palavra == 'enquanto':
                tokens.append(('ENQUANTO', palavra))
            elif palavra == 'interromper':
                tokens.append(('INTERROMPER', palavra))
            elif palavra == 'continuar':
                tokens.append(('CONTINUAR', palavra))
            elif palavra == 'imprimir':
                tokens.append(('IMPRIMIR', palavra))
            elif palavra == 'inteiro':
                tokens.append(('INTEIRO', palavra))
            elif palavra == 'booleano':
                tokens.append(('BOOLEANO', palavra))
            elif palavra == 'vazio':
                tokens.append(('VAZIO', palavra))
            elif palavra == 'retornar':
                tokens.append(('RETORNAR', palavra))
            else:
                tokens.append(('ID', palavra))
        elif codigo_fonte[pos].isdigit():
            inicio = pos
            while pos < length and codigo_fonte[pos].isdigit():
                pos += 1
            tokens.append(('NUMERO', int(codigo_fonte[inicio:pos])))
        else:
            print(f"Erro: Caractere invalido '{codigo_fonte[pos]}' na posicao {pos+1}")
            pos += 1

    return tokens

# # Codigo fonte
# codigo_fonte = """
# variavel_inteira = 5
# variavel_booleana = verdadeiro

# funcao imprimir_ola():
#     imprimir("Ola, Mundo!")

# funcao somar(a, b):
#     retornar a + b

# resultado = 0

# imprimir_ola()

# resultado = somar(3, 4)

# se resultado > 10:
#     imprimir("Resultado e maior que 10.")
# senao:
#     imprimir("Resultado e 10 ou menor.")

# contador = 0
# enquanto contador < resultado:
#     imprimir(f"Contando: {contador}")
#     contador += 1

#     se contador == 5:
#         imprimir("Pulando 5")
#         continuar
    
#     se contador == 7:
#         imprimir("Parando no 7")
#         interromper

# MINHA_CONSTANTE = "Esta e uma constante"
# imprimir(MINHA_CONSTANTE)

# imprimir(f"Variável booleana: {variavel_booleana}")

# resultado_aritmetico = (variavel_inteira + resultado) - 5 * 2 / 2

# se resultado_aritmetico == 10 ou (variavel_inteira != 5 e variavel_booleana e resultado <= 10):
#     imprimir("Alguma condicao booleana foi atendida.")
# """

# tokens = analisador_lexico(codigo_fonte)