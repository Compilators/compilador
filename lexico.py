def analisador_lexico(codigo_fonte):
    tokens = []
    pos = 0
    linha = 1
    length = len(codigo_fonte)
    while pos < length:
        if codigo_fonte[pos] in ' \t':
            pos += 1
        if codigo_fonte[pos] == '\n':
            pos += 1
            linha += 1
        elif codigo_fonte[pos] == '+':
            tokens.append(('MAIS', '+', linha))
            pos += 1
        elif codigo_fonte[pos] == '-':
            tokens.append(('MENOS', '-', linha))
            pos += 1
        elif codigo_fonte[pos] == '*':
            tokens.append(('VEZES', '*', linha))
            pos += 1
        elif codigo_fonte[pos] == '/':
            tokens.append(('DIVIDE', '/', linha))
            pos += 1
        elif codigo_fonte[pos] == '=':
            if pos + 1 < len(codigo_fonte) and codigo_fonte[pos + 1] == '=':
                tokens.append(('IGUAL', '==', linha))
                pos += 2
            else:
                tokens.append(('ATRIBUICAO', '=', linha))
            pos += 1
        elif codigo_fonte[pos] == '!':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('DIFERENTE', '!=', linha))
                pos += 2
            else:
                print(f"Erro: Caractere inesperado '{codigo_fonte[pos]}' na posicao {pos+1}")
                pos += 1
        elif codigo_fonte[pos] == '>':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MAIOR_IGUAL', '>=', linha))
                pos += 2
            else:
                tokens.append(('MAIOR', '>', linha))
                pos += 1
        elif codigo_fonte[pos] == '<':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MENOR_IGUAL', '<=', linha))
                pos += 2
            else:
                tokens.append(('MENOR', '<', linha))
                pos += 1
        elif codigo_fonte[pos] == '(':
            tokens.append(('ABRE_PARENTESE', '(', linha))
            pos += 1
        elif codigo_fonte[pos] == ')':
            tokens.append(('FECHA_PARENTESE', ')', linha))
            pos += 1
        elif codigo_fonte[pos] == ',':
            tokens.append(('VIRGULA', ',', linha))
            pos += 1
        elif codigo_fonte[pos] == ':':
            tokens.append(('DOIS_PONTOS', ':', linha))
            pos += 1
        elif codigo_fonte[pos] == '{':
            tokens.append(('ABRE_CHAVE', '{', linha))
            pos += 1
        elif codigo_fonte[pos] == '}':
            tokens.append(('FECHA_CHAVE', '}', linha))
            pos += 1
        elif codigo_fonte[pos] == '"':
            inicio = pos
            pos += 1
            while pos < length and codigo_fonte[pos] != '"':
                pos += 1
            if pos < length and codigo_fonte[pos] == '"':
                tokens.append(('STRING', codigo_fonte[inicio + 1:pos], linha))
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
                tokens.append(('BOOLEANO', palavra, linha))
            elif palavra == 'funcao':
                tokens.append(('FUNCAO', palavra, linha))
            elif palavra == 'se':
                tokens.append(('SE', palavra, linha))
            elif palavra == 'senao':
                tokens.append(('SENAO', palavra, linha))
            elif palavra == 'enquanto':
                tokens.append(('ENQUANTO', palavra, linha))
            elif palavra == 'interromper':
                tokens.append(('INTERROMPER', palavra, linha))
            elif palavra == 'continuar':
                tokens.append(('CONTINUAR', palavra, linha))
            elif palavra == 'imprimir':
                tokens.append(('IMPRIMIR', palavra, linha))
            elif palavra == 'inteiro':
                tokens.append(('INTEIRO', palavra, linha))
            elif palavra == 'booleano':
                tokens.append(('BOOLEANO', palavra, linha))
            elif palavra == 'vazio':
                tokens.append(('VAZIO', palavra, linha))
            elif palavra == 'retornar':
                tokens.append(('RETORNAR', palavra, linha))
            else:
                tokens.append(('ID', palavra, linha))
        elif codigo_fonte[pos].isdigit():
            inicio = pos
            while pos < length and codigo_fonte[pos].isdigit():
                pos += 1
            tokens.append(('NUMERO', int(codigo_fonte[inicio:pos]), linha))
        else:
            # print(f"Erro: Caractere invalido '{codigo_fonte[pos]}' na posicao {pos+1}")
            pos += 1
        
    return tokens