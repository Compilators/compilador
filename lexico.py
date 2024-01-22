def analisador_lexico(codigo_fonte):
    tokens = []
    pos = 0
    linha = 1
    length = len(codigo_fonte)
    while pos < length:
        while codigo_fonte[pos] in ' \t':
            pos += 1
        if codigo_fonte[pos] == '\n':
            pos += 1
            linha += 1
        elif codigo_fonte[pos] == '+':
            tokens.append(('MAIS', '+', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '-':
            tokens.append(('MENOS', '-', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '*':
            tokens.append(('VEZES', '*', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '/':
            tokens.append(('DIVIDE', '/', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '=':
            if pos + 1 < len(codigo_fonte) and codigo_fonte[pos + 1] == '=':
                tokens.append(('IGUAL', '==', f'linha: {linha}'))
                pos += 2
            else:
                tokens.append(('ATRIBUICAO', '=', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '!':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('DIFERENTE', '!=', f'linha: {linha}'))
                pos += 2
            else:
                print(f"Erro: Caractere inesperado '{codigo_fonte[pos]}' na posicao {pos+1}")
                pos += 1
        elif codigo_fonte[pos] == '>':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MAIOR_IGUAL', '>=', f'linha: {linha}'))
                pos += 2
            else:
                tokens.append(('MAIOR', '>', f'linha: {linha}'))
                pos += 1
        elif codigo_fonte[pos] == '<':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MENOR_IGUAL', '<=', f'linha: {linha}'))
                pos += 2
            else:
                tokens.append(('MENOR', '<', f'linha: {linha}'))
                pos += 1
        elif codigo_fonte[pos] == '(':
            tokens.append(('ABRE_PARENTESE', '(', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == ')':
            tokens.append(('FECHA_PARENTESE', ')', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == ',':
            tokens.append(('VIRGULA', ',', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == ':':
            tokens.append(('DOIS_PONTOS', ':', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '{':
            tokens.append(('ABRE_CHAVE', '{', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '}':
            tokens.append(('FECHA_CHAVE', '}', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '"':
            inicio = pos
            pos += 1
            while pos < length and codigo_fonte[pos] != '"':
                pos += 1
            if pos < length and codigo_fonte[pos] == '"':
                tokens.append(('STRING', codigo_fonte[inicio + 1:pos], f'linha: {linha}'))
                pos += 1
            else:
                print(f"Erro: String nao terminada, começando na posicao {inicio+1}")
        elif codigo_fonte[pos].isalpha() or codigo_fonte[pos] == '_':
            inicio = pos
            pos += 1
            while pos < length and (codigo_fonte[pos].isalnum() or codigo_fonte[pos] == '_'):
                pos += 1
            palavra = codigo_fonte[inicio:pos]
            # tabela_simbolos.adicionar_simbolo(palavra, tabela_simbolos.verifica_tipo(palavra), linha)
            if palavra == 'verdadeiro' or palavra == 'falso':
                tokens.append(('BOOLEANO', palavra, f'linha: {linha}'))
            elif palavra == 'funcao':
                tokens.append(('FUNCAO', palavra, f'linha: {linha}'))
            elif palavra == 'se':
                tokens.append(('SE', palavra, f'linha: {linha}'))
            elif palavra == 'senao':
                tokens.append(('SENAO', palavra, f'linha: {linha}'))
            elif palavra == 'enquanto':
                tokens.append(('ENQUANTO', palavra, f'linha: {linha}'))
            elif palavra == 'interromper':
                tokens.append(('INTERROMPER', palavra, f'linha: {linha}'))
            elif palavra == 'continuar':
                tokens.append(('CONTINUAR', palavra, f'linha: {linha}'))
            elif palavra == 'imprimir':
                tokens.append(('IMPRIMIR', palavra, f'linha: {linha}'))
            elif palavra == 'inteiro':
                tokens.append(('INTEIRO', palavra, f'linha: {linha}'))
            elif palavra == 'booleano':
                tokens.append(('BOOLEANO', palavra, f'linha: {linha}'))
            elif palavra == 'vazio':
                tokens.append(('VAZIO', palavra, f'linha: {linha}'))
            elif palavra == 'retornar':
                tokens.append(('RETORNAR', palavra, f'linha: {linha}'))
            else:
                tokens.append(('ID', palavra, f'linha: {linha}'))
        elif codigo_fonte[pos].isdigit():
            inicio = pos
            while pos < length and codigo_fonte[pos].isdigit():
                pos += 1
            tokens.append(('NUMERO', int(codigo_fonte[inicio:pos]), f'linha: {linha}'))
        else:
            raise Exception(f"Erro: Caractere invalido '{codigo_fonte[pos]}' na posicao {pos+1}")
    return tokens