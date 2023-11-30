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
            if pos + 1 < len(codigo_fonte) and codigo_fonte[pos + 1] == '=':
                tokens.append(('IGUAL', '=='))
                pos += 2
            else:
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
        elif codigo_fonte[pos] == '{':
            tokens.append(('ABRE_CHAVE', '{'))
            pos += 1
        elif codigo_fonte[pos] == '}':
            tokens.append(('FECHA_CHAVE', '}'))
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